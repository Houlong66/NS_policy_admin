<template>
  <div>
    <div class="relationlist-container">
      <div>
        <!-- 搜索栏 -->
        <el-row type="flex" justify="end">
          <el-col :span="10" style="text-align:end">
            <el-button type="primary" @click="handleCreate({})">新建关系</el-button>
          </el-col>
        </el-row>

        <div style="height:20px;"></div>

        <!-- 表格栏 -->
        <div class="table-container">
          <cm-table :list="pagedList" :total="total" :options="options" :pagination="pagination" :columns="columns"
            :operates="operates" @handleSizeChange="handleSizeChange" @handleIndexChange="handleIndexChange"></cm-table>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import table from './table'
export default {
  name: 'RelationList',
  data() {
    return {
      formData: {}, // 选中的数据，空对象则为新建
      list: [],
      columns: table.columns,
      operates: table.operates,
      total: 0,
      pagination: table.pagination,
      options: table.options
    }
  },
  created() {
    this.initData()
  },
  computed: {
    pagedList() {
      let index = this.pagination.pageIndex
      let size = this.pagination.pageSize
      return this.list.slice((index - 1) * size, index * size)
    }
  },
  methods: {
    // 初始化数据
    initData() {
      const resources = [{ name: 'relations' }]
      const options = { resources }
      this.api.restful(options).then(res => {
        if (res.code === 200) {
          this.list = res.data
          this.total = this.list.length
        }
      })
    },
    // 切换每页显示的数量
    handleSizeChange(pagination) {
      this.pagination = pagination
    },
    // 切换页码
    handleIndexChange(pagination) {
      this.pagination = pagination
    },
    // 编辑
    handleCreate(item) {
      this.formData = item
      this.showCreate = true
    },
    // 删除
    handleDelete(item) {
      this.$confirm('确定删除该关系吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
      }).catch()
    },
  }
}
</script>

<style lang="scss" scoped>
/deep/ .el-table .cell {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  overflow: hidden;
}
</style>