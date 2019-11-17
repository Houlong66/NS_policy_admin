<template>
  <div>
    <div class="industrylist-container">
      <el-tree :data="list" default-expand-all :expand-on-click-node="false">
        <span class="custom-tree-node" slot-scope="{ node, data }">
          <span>{{ node.label }}</span>
          <span>
            <el-button v-if="node.level!==3" type="text" size="mini" @click="()=>append(data, node)">
              新增子行业
            </el-button>
            <el-button v-if="node.level!==1" type="text" size="mini" @click="()=>modify(data, node)">
              修改
            </el-button>
            <el-button v-if="node.level!==1" type="text" size="mini" @click="()=>remove(data, node)">
              删除
            </el-button>
          </span>
        </span>
      </el-tree>
    </div>

  </div>
</template>

<script>
export default {
  name: 'IndustryList',
  data() {
    return {
      list: []
    }
  },
  created() {
    this.initData()
  },
  computed: {

  },
  methods: {
    // 初始化数据
    initData() {
      const resources = [{ name: 'industries' }]
      const options = { resources }
      this.api.restful(options).then(res => {
        if (res.code === 200) {
          this.list = res.data
        }
      })
    },
    // 提交更新请求
    async submit(node) {
      const level = node.level
      let copyNode = node
      for (let i = 1; i < level; i++) {
        copyNode = copyNode.parent
      }
      let submitData = copyNode.data
      const resources = [{ name: 'industries' }]
      submitData = JSON.stringify(submitData)
      const data = {data: submitData}
      const options = { resources, method:'post', data }
      let res = await this.api.restful(options)
      if (res.code === 200) {
        this.$message.success('操作成功！')
      }
    },
    // 增加节点
    async append(nodeData, node) {
      try {
        let {value} = await this.$prompt('请输入新增行业名称', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputValidator: (e) => !!e,
          inputErrorMessage: '名称不能为空'
        })
        if (!nodeData.children) {
          this.$set(nodeData, 'children', [])
        }
        nodeData.children.push({label: value})
        this.submit(node)
      }
      catch (e) {console.log(e)}
    },
    // 修改行业名称
    async modify(nodeData,node) {
      try {
        let {value} = await this.$prompt('请输入行业名称', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputValue: nodeData.label,
          inputValidator: (e) => !!e,
          inputErrorMessage: '名称不能为空'
        })
        nodeData.label=value
        this.submit(node)
      }
      catch(e) {console.log(e)}
    },
    // 删除
    async remove(nodeData, node) {
      try {
        await this.$confirm('确定删除该行业吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
        const parent = node.parent
        const children = parent.data.children
        const nodeIndex = children.findIndex(e => e == nodeData)
        children.splice(nodeIndex,1)
        this.submit(node)
      } catch (e) { console.log(e) }
    },
  }
}
</script>

<style lang="scss" scoped>
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
</style>