const _import = require('./_import_' + process.env.NODE_ENV)

const routes = [{
  path: '/',
  redirect: 'main',
  name: '',
  meta: {
    requireAuth: true
  },
  component: _import('layout/index'),
  children: [{
    path: '/main',
    name: 'Main',
    meta: {
      routeText: '首页',
      routeIcon: 'el-icon-goods',
      showSideBar: true
    },
    component: _import('main/index/index')
  }]
},
{
  path: '/relation',
  component: _import('layout/index'),
  meta: {
    requireAuth: true
  },
  children: [{
    path: 'relationlist',
    name: 'RelationList',
    meta: {
      routeText: '关系管理',
      routeIcon: 'el-icon-location',
      showSideBar: true,
      keepAlive: true
    },
    component: _import('main/relation/RelationList/index')
  }]
},
{
  path: '/industry',
  component: _import('layout/index'),
  meta: {
    requireAuth: true
  },
  children: [{
    path: 'industrylist',
    name: 'IndustryList',
    meta: {
      routeText: '行业管理',
      routeIcon: 'el-icon-location',
      showSideBar: true,
      keepAlive: true
    },
    component: _import('main/industry/IndustryList/index')
  }]
},
{
  path: '/dict',
  component: _import('layout/index'),
  meta: {
    requireAuth: true
  },
  children: [{
    path: 'dictlist',
    name: 'DictList',
    meta: {
      routeText: '数据字典管理',
      routeIcon: 'el-icon-location',
      showSideBar: true,
      keepAlive: true
    },
    component: _import('main/dict/DictList/index')
  }]
},
{
  path: '/rule',
  component: _import('layout/index'),
  meta: {
    requireAuth: true
  },
  children: [{
    path: 'rulelist',
    name: 'RuleList',
    meta: {
      routeText: '匹配规则管理',
      routeIcon: 'el-icon-location',
      showSideBar: true,
      keepAlive: true
    },
    component: _import('main/rule/RuleList/index')
  }]
},
]

export default routes