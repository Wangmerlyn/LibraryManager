import Footer from '@/components/Footer';
import { currentUser, login } from '@/services/ant-design-pro/api';
import { getFakeCaptcha } from '@/services/ant-design-pro/login';
import {
    AlipayCircleOutlined,
    LockOutlined,
    MobileOutlined,
    TaobaoCircleOutlined,
    UserOutlined,
    WeiboCircleOutlined,
} from '@ant-design/icons';
import {
    LoginForm,
    ProForm,
    ProFormCaptcha,
    ProFormCheckbox,
    ProFormText,
} from '@ant-design/pro-components';
import { Access, FormattedMessage, history, SelectLang, useAccess, useIntl, useModel } from '@umijs/max';
import { Alert, message, Tabs } from 'antd';
import React, { useState } from 'react';
import styles from './index.less';
import logo from '../../assets/images/logo1.jpg'

const LoginMessage: React.FC<{
    content: string;
}> = ({ content }) => {
    return (
        <Alert
            style={{
                marginBottom: 24,
            }}
            message={content}
            type="error"
            showIcon
        />
    );
};

const Login: React.FC = () => {
    const [userLoginState, setUserLoginState] = useState<API.LoginResult>({});
    const [type, setType] = useState<string>('account');
    const { initialState, setInitialState } = useModel('@@initialState');
    const access = useAccess();

    const intl = useIntl();

    const fetchUserInfo = async () => {
        const userInfo = await initialState?.fetchUserInfo?.();
        console.log("fetch_initialState:")
        console.log(initialState)
        console.log("fetch_userInfo")
        console.log(userInfo)
        if (userInfo) {
            setInitialState((s) => ({
                ...s,
                currentUser: userInfo,
            }));
            console.log(initialState?.currentUser)
        }
        console.log("fetch_userInfo")
        console.log(initialState)
    };

    const handleSubmit = async (values: API.LoginParams) => {
        try {
            // 登录
            console.log("initialState before login:")
            console.log(initialState)
            const msg = await login({ ...values, type });
            console.log("initialState after login:")
            console.log(initialState)
            await setInitialState((s) => {
                return {
                    ...s,
                    currentUser: { ...s?.currentUser, access: msg['identity'] }
                }
            })
            console.log("initialState after set initialstate:")
            console.log(initialState)

            if (msg['success'] === true) {
                const defaultLoginSuccessMessage = intl.formatMessage({
                    id: 'pages.login.success',
                    defaultMessage: '登录成功！',
                });
                message.success(defaultLoginSuccessMessage);
                await fetchUserInfo();
                // const urlParams = new URL(window.location.href).searchParams;
                // '/' 在 routes.ts 里被重定向到 '/welcome'
                history.push('/');
                return;
            }
            // 如果失败去设置用户错误信息
            setUserLoginState(msg);
        } catch (error) {
            const defaultLoginFailureMessage = intl.formatMessage({
                id: 'pages.login.failure',
                defaultMessage: '登录失败，请重试！',
            });
            message.error(defaultLoginFailureMessage);
        }
    };
    const { status, type: loginType } = userLoginState;

    return (
        <div className={styles.container}>
            <div className={styles.lang} data-lang>
                {SelectLang && <SelectLang />}
            </div>
            <div className={styles.content}>
                <LoginForm
                    logo={<img alt="logo" src={logo} />}
                    title="图书管理系统"
                    subTitle={intl.formatMessage({ id: 'pages.layouts.userLayout.title' })}
                    initialValues={{
                        autoLogin: true,
                    }}
                    onFinish={async (values) => {
                        console.log("login values:")
                        console.log(values);
                        console.log("initialstate before handle in")
                        console.log(initialState)
                        await handleSubmit(values as API.LoginParams);
                    }}
                >
                    <Tabs activeKey={type} onChange={setType}>
                        <Tabs.TabPane
                            key="account"
                            tab={intl.formatMessage({
                                id: 'pages.login.accountLogin.tab',
                                defaultMessage: '账户密码登录',
                            })}
                        />
                    </Tabs>

                    {status === 'error' && loginType === 'account' && (
                        <LoginMessage
                            content={intl.formatMessage({
                                id: 'pages.login.accountLogin.errorMessage',
                                defaultMessage: '账户或密码错误(admin/ant.design)',
                            })}
                        />
                    )}
                    {type === 'account' && (
                        <>
                            <ProFormText
                                name="username"
                                fieldProps={{
                                    size: 'large',
                                    prefix: <UserOutlined className={styles.prefixIcon} />,
                                }}
                                placeholder={intl.formatMessage({
                                    id: 'pages.login.username.placeholder',
                                    defaultMessage: '用户名: admin or user',
                                })}
                                rules={[
                                    {
                                        required: true,
                                        message: (
                                            <FormattedMessage
                                                id="pages.login.username.required"
                                                defaultMessage="请输入用户名!"
                                            />
                                        ),
                                    },
                                ]}
                            />
                            <ProFormText.Password
                                name="password"
                                fieldProps={{
                                    size: 'large',
                                    prefix: <LockOutlined className={styles.prefixIcon} />,
                                }}
                                placeholder={intl.formatMessage({
                                    id: 'pages.login.password.placeholder',
                                    defaultMessage: '密码: admin123',
                                })}
                                rules={[
                                    {
                                        required: true,
                                        message: (
                                            <FormattedMessage
                                                id="pages.login.password.required"
                                                defaultMessage="请输入密码！"
                                            />
                                        ),
                                    },
                                ]}
                            />
                        </>
                    )}

                    <div
                        style={{
                            marginBottom: 24,
                        }}
                    >
                        <ProFormCheckbox noStyle name="autoLogin">
                            <FormattedMessage id="pages.login.rememberMe" defaultMessage="自动登录" />
                        </ProFormCheckbox>
                        {/* <a
              style={{
                float: 'right',
              }}
            >
              <FormattedMessage id="pages.login.forgotPassword" defaultMessage="忘记密码" />
            </a> */}
                    </div>
                </LoginForm>
                {/* <ProForm onFinish={async (values) => {
                    console.log(values);
                }}>
                    <ProFormText label="测试" name="ad" placeholder="请输入" rules={[{ required: true, message: '测试不能为空' }]} />
                </ProForm> */}
            </div>
            <Footer />
        </div>
    );
};

export default Login;
