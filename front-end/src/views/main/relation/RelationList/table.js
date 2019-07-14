const columns = [
  {
    prop: 'company_id',
    label: '企业id',
    align: 'center'
  },
  {
    prop: 'guide_id',
    label: '政策id',
    align: 'center'
  },
  {
    prop: 'matching',
    label: '匹配度',
    align: 'center'
  },
  {
    prop: 'reason',
    label: '匹配内容',
    align: 'center'
  },
] // 需要展示的列

const operates = {
  width: 200,
  list: [
    {
      label: '编辑',
      type: 'warning',
      icon: 'el-icon-edit',
      method: ({index, row,vm}) => {
        vm.handleCreate(row)
      }
    },
    {
      label: '删除',
      type: 'danger',
      icon: 'el-icon-delete',
      method: ({index, row,vm}) => {
        vm.handleDelete(row)
      }
    }
  ]
} // 操作按钮组

const pagination = {
  pageIndex: 1,
  pageSize: 20,
} // 分页参数
const options = {
  stripe: true, // 是否为斑马纹 table
  loading: false, // 是否添加表格loading加载动画
  highlightCurrentRow: true, // 是否支持当前行高亮显示
  mutiSelect: false // 是否支持列表项选中功能
} // table 的参数

export default {
  columns,
  operates,
  pagination,
  options
}