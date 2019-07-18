<template>
  <el-dialog :visible.sync="showTemp" :title="titleText" width="30%">
    <el-form :model="form" :rules="rules" ref="form" label-width="120px" v-if="showTemp">
      <el-form-item v-for="(key, index) in formKeys" :key="index" :label="key.label" :prop="key.value">
        <el-input v-if="key.type==='input'" v-model="form[key.value]" :placeholder="'请填写'+key.label" style="width:60%"
          :readonly="key.readonly">
        </el-input>
        <el-select v-if="key.type==='select'" v-model="form[key.value]" :placeholder="'请填写'+key.label"
          :multiple="key.multiple" :filterable="key.filterable" :allow-create="key.allowCreate"
          :default-first-option="key.defaultFirstOption">
          <el-option v-for="(item,i) in items[key.value]" :key="i" :label="item" :value="item"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">{{buttonText}}</el-button>
        <el-button @click="showTemp=false">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
// mixins
export default {
  props: {
    show: Boolean,
    formData: Object,
    isEdit: Boolean,
    list: Array
  },
  data() {
    return {
      showTemp: false,
      form: {},
      formKeys: [
        { label: '关键词', value: 'word', type: 'select', multiple: true, filterable: true, allowCreate: true, defaultFirstOption: true },
        { label: '类型', value: 'type', type: 'select' },
        { label: '优先级', value: 'priority', type: 'input' },
        { label: '关系', value: 'relation', type: 'select' }
      ],
      items: {
        word: [],
        type: ['数字', '地址', '一般'],
        relation: ['大于', '小于', '位于', '是', '否']
      }
    }
  },
  computed: {
    checkPriority() {
      return (rule, value, callback) => {
        if (this.list.find(item => item.priority == value)) callback(new Error('这个优先级已经存在'))
        callback()
      }
    },
    titleText() {
      return (this.isEdit) ? '修改关系' : '新增关系'
    },
    buttonText() {
      return (this.isEdit) ? '确认修改' : '确认创建'
    },
    rules() {
      let tempRules = {}
      this.formKeys.forEach(key => {
        tempRules[key.value] = [{ required: true, message: `请填写${key.label}` }]
        if (key.value === 'priority') tempRules[key.value].push({ validator: this.checkPriority, trigger: 'blur' })
      })
      return tempRules
    }
  },
  watch: {
    show(val) {
      this.showTemp = val
    },
    showTemp(val) {
      this.$emit('update:show', val)
    },
    formData(val) {
      this.formKeys.forEach(key => {
        this.$set(this.form, key.value, val[key.value])
      })
    },
  },
  methods: {
    onSubmit() {
      this.$refs['form'].validate(async valid => {
        if (valid) {
          const resources = [{ name: 'relations' }]
          const method = this.isEdit ? 'put' : 'post'
          let data = this.form
          if (this.isEdit) data.relation_id = this.formData['_id']
          const options = { resources, method, data }
          let res = await this.api.restful(options)
          if (res.code === 200) {
            this.$message.success('操作成功！')
            this.$emit('afterCreate')
            this.showTemp = false
          }
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>