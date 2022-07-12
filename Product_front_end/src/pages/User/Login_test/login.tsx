import { login } from '@/services/ant-design-pro/api';
import { Alert } from 'antd';

// 输出登陆失败的信息
const LoginMessage: React.FC<{
    content: string;
  }>= ({ content }) => {
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
    
    
    return (
        <>
        <head>
            <meta charSet="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hook</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/shorthandcss@1.1.1/dist/shorthand.min.css" />
            <link rel="stylesheet"
                href="https://fonts.googleapis.com/css?family=Muli:200,300,400,500,600,700,800,900&display=swap" />
            <link rel="stylesheet" type="text/css"
                href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.css" />
            <link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css" />
        </head>
        
        <body className="bg-black muli">
            <nav className="w-100pc flex flex-column md-flex-row md-px-10 py-5 bg-black">
                <div className="flex justify-between">
                    <a href="#" className="flex items-center p-2 mr-4 no-underline">
                        <img className="max-h-l2 w-auto" src="img/logo1.jpg" />
                    </a>
                    <a data-toggle="toggle-nav" data-target="#nav-items" href="#"
                        className="flex items-center ml-auto md-hidden indigo-lighter opacity-50 hover-opacity-100 ease-300 p-1 m-3">
                        <i data-feather="menu"></i>
                    </a>
                </div>
                <div id="nav-items" className="hidden flex sm-w-100pc flex-column md-flex md-flex-row md-justify-end items-center">
                    <a href="index.html" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Home</a>
                    <a href="#features" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Features</a>
                    <a href="#pricing" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Pricing</a>
                    <a href="#blog" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Blog</a>
                </div>
            </nav>

            <section id="login" className="py-l10">
                <div className="flex flex-column md-flex-row md-w-80pc mx-auto">
                    <div className="w-100pc md-w-50pc">
                        <div className="br-8 p-5 m-5 bg-indigo-lightest-10 pointer hover-scale-up-1 ease-300">
                            <div className="inline-block bg-indigo indigo-lightest br-10 px-10 py-1 mb-10 fs-s4 uppercase">
                                USER
                            </div>
                            <div className="indigo-lightest fw-600 fs-m1">
                                NAME: 
                            </div>
                            <input type="text" id='username' placeholder="Name"/>
                            <div className="indigo-lightest fw-600 fs-m1">
                                PASSWORD: 
                            </div>
                            <input type="text" id='password' placeholder="PASSWORD"/><br/>
                            {/* <button onClick={()=>{alert($("username").val())}} className="mt-10 button bg-black fs-s3 white no-underline">Log in</button> */}
                            <a href="#" className="mt-10 button bg-black fs-s3 white no-underline">Log in</a>
                            <a href="#" className="mt-10 button bg-black fs-s3 white no-underline">Forget PASSWORD</a>
                            <script>
                                var veritoken = (document.getElementsByName('__RequestVerificationToken')[0] as HTMLInputElement).value
                                console.log(veritoken)
                            </script>

                        </div>
                    </div>

                    <div className="w-100pc md-w-50pc">
                        <div className="br-8 p-5 m-5 bg-indigo-lightest-10  pointer hover-scale-up-1 ease-300">
                            <div className="inline-block bg-indigo indigo-lightest br-3 px-4 py-1 mb-10 fs-s4 uppercase">
                                ADMIN
                            </div>
                            <div className="indigo-lightest fw-600 fs-m1">
                                NAME: 
                            </div>
                            <input type="text" placeholder="Name"/>
                            <div className="indigo-lightest fw-600 fs-m1">
                                PASSWORD:
                            </div>
                            <input type="text" placeholder="Password"/><br/>
                            <a href="#for_admin" className="mt-10 button bg-black fs-s3 white no-underline">Read</a>
                            <a href="#" className="mt-10 button bg-black fs-s3 white no-underline">Forget PASSWORD</a>
                        </div>
                    </div>
                </div>
            </section>

            <a className="fixed top-50pc right-0 p-3 bg-indigo white hover-scale-up-1 ease-300 no-underline"
                href="https://gum.co/tifJM" target="_blank"> 
            <i className="w-4" data-feather="download"></i>
            </a>
            <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
            <script src="https://unpkg.com/feather-icons"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.js"></script>
            <script
                src="https://cdn.jsdelivr.net/gh/cferdinandi/smooth-scroll@15.0.0/dist/smooth-scroll.polyfills.min.js"></script>
            <script src="assets/js/script.js"></script>
        </body>
        </>
    )
}

export default Login