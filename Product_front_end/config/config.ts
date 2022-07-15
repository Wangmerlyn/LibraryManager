// https://umijs.org/config/
import { defineConfig } from '@umijs/max';
import { join } from 'path';
import defaultSettings from './defaultSettings';
import proxy from './proxy';
import routes from './routes';

const { REACT_APP_ENV } = process.env;

export default defineConfig({
  headScripts: [],
  links: [{href: "https://cdn.jsdelivr.net/npm/shorthandcss@1.1.1/dist/shorthand.min.css", rel: "stylesheet"},
    {rel: "stylesheet",
    href: "https://fonts.googleapis.com/css?family=Muli:200,300,400,500,600,700,800,900&display=swap"},
    {rel:"stylesheet",type:"text/css",
    href:"https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.css"},
    {rel:"stylesheet",type:"text/css",href:"//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"}],
  
  metas: [{charSet:"UTF-8"},{name:"viewport",content: "width=device-width, initial-scale=1.0"}],
  hash: true,
  antd: {
    dark: true,
    compact: true,
  },
  request: {},
  initialState: {},
  model: {},
  layout: {
    // https://umijs.org/zh-CN/plugins/plugin-layout
    locale: false,
    siderWidth: 208,
    ...defaultSettings,
  },
  // https://umijs.org/zh-CN/plugins/plugin-locale
  locale: {
    // default zh-CN
    default: 'zh-CN',
    antd: true,
    // default true, when it is true, will use `navigator.language` overwrite default
    baseNavigator: true,
  },

  targets: {
    ie: 11,
  },
  // umi routes: https://umijs.org/docs/routing
  routes,
  access: {},
  // Theme for antd: https://ant.design/docs/react/customize-theme-cn
  theme: {
    // 如果不想要 configProvide 动态设置主题需要把这个设置为 default
    // 只有设置为 variable， 才能使用 configProvide 动态设置主色调
    // https://ant.design/docs/react/customize-theme-variable-cn
    'root-entry-name': 'variable',
  },
  ignoreMomentLocale: true,
  proxy: proxy[REACT_APP_ENV || 'dev'],
  manifest: {
    basePath: '/',
  },
  // Fast Refresh 热更新
  fastRefresh: true,
  presets: ['umi-presets-pro'],
  openAPI: [
    {
      requestLibPath: "import { request } from '@umijs/max'",
      // 或者使用在线的版本
      // schemaPath: "https://gw.alipayobjects.com/os/antfincdn/M%24jrzTTYJN/oneapi.json"
      schemaPath: join(__dirname, 'oneapi.json'),
      mock: false,
    },
    {
      requestLibPath: "import { request } from '@umijs/max'",
      schemaPath: 'https://gw.alipayobjects.com/os/antfincdn/CA1dOm%2631B/openapi.json',
      projectName: 'swagger',
    },
  ],
});
