import { GithubOutlined } from '@ant-design/icons';
import { DefaultFooter } from '@ant-design/pro-components';
import { useIntl } from '@umijs/max';

const Footer: React.FC = () => {
  const intl = useIntl();
  const defaultMessage = intl.formatMessage({
    id: 'app.copyright.produced',
    defaultMessage: 'published by AI XJTU',
  });

  const currentYear = new Date().getFullYear();

  return (
    <DefaultFooter
      style={{
        background: 'none',
      }}
      copyright={`${currentYear} ${defaultMessage}`}
      links={[
        {
          key: 'XJTU',
          title: 'XJTU',
          href: 'http://www.xjtu.edu.cn/',
          blankTarget: true,
        },
        {
          key: 'github',
          title: <GithubOutlined />,
          href: 'https://github.com/Wangmerlyn/LibraryManager',
          blankTarget: true,
        },
        {
          key: 'IAIR',
          title: 'IAIR',
          href: 'http://www.aiar.xjtu.edu.cn/',
          blankTarget: true,
        },
      ]}
    />
  );
};

export default Footer;
