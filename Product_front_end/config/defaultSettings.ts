import { Settings as LayoutSettings } from '@ant-design/pro-components';

const Settings: LayoutSettings & {
  pwa?: boolean;
  logo?: string;
} = {
  "title": "Library Manager",
  "navTheme": "realDark",
  "primaryColor": "#1890ff",
  "layout": "mix",
  "contentWidth": "Fluid",
  "fixedHeader": false,
  "fixSiderbar": true,
  "pwa": false,
  "headerHeight": 56,
  "headerTheme" : 'dark',
  "menu":{
    locale: false,
  },
};

export default Settings;
