import component from "@/locales/bn-BD/component";

export default [
  {
    path: '/user',
    layout: false,
    routes: [
      {
        name: '登录',
        path: '/user/login',
        component: './User/Login',
      },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/welcome',
    name: '欢迎',
    icon: 'home',
    component: './Welcome',
  },
  {
    path: '/admin',
    name: '管理员界面',
    icon: 'crown',
    access: 'canAdmin',
    routes: [
      {
        path: '/admin/book',
        name: '书籍管理',
        icon: 'smile',
        component: './Book',
      },
      // {
      //   path: '/admin/example',
      //   name: '例子',
      //   icon: 'smile',
      //   component: './TableList',
      // },
      {
        component: './404',
      },
    ],
  },
  {
    path: '/user/book',
    name: '书籍查询',
    icon: 'book',
    component: './Book',
  },
  {
    path: '/about_us',
    name: '关于我们',
    icon: 'smile',
    component: './About_us',
  },
  {
    path: '/features',
    name: '特点',
    icon: 'star',
    component: './Features',
  },
  {
    path: '/',
    redirect: '/welcome',
  },
  {
    component: './404',
  },
];
