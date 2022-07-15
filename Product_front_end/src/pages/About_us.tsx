import React from "react"
import logo1 from './assets/images/logo1.jpg'
import logo from "./assets/images/6.png"

const About_us: React.FC = () => {
    return (
    <>
        <div className="bg-black muli">
            <nav className="w-100pc flex flex-column md-flex-row md-px-10 py-5 bg-black">
                <div className="flex justify-between">
                    <a href="#" className="flex items-center p-2 mr-4 no-underline">
                        <img className="max-h-l3 w-auto" src={logo1} />
                    </a>
                    <a data-toggle="toggle-nav" data-target="#nav-items" href="#"
                        className="flex items-center ml-auto md-hidden indigo-lighter opacity-50 hover-opacity-100 ease-300 p-1 m-3">
                        <i data-feather="menu"></i>
                    </a>
                </div>
                <div id="nav-items" className="hidden flex sm-w-100pc flex-column md-flex md-flex-row md-justify-end items-center">
                    <a href="../welcome" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Home</a>
                    <a href="../features" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Features</a>
                    <a href="https://github.com/Wangmerlyn/LibraryManager" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Github</a>
                    <a href="../about_us" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">About Us</a>

                </div>
            </nav>

            <section className="p-10 md-p-l5" >
                <div className="md-w-80pc">
                    <h2 className="white fs-l3 fw-900 lh-1">About Us</h2>
                    <p className="indigo-lightest fw-350 fs-m1 opacity-80 my-7">
                        我们是一支由九位西安交通大学人工智能专业学生组成的团队，在12天的实习过程中，从零开始，在中国电信陕西公众信息产业有限公司指导老师的帮助下，设计并实现了功能较为完备的图书管理系统。
                    </p><br/>
                </div>


                <div><img src={logo}   width="370"/></div>

                <div className="w-150pc md-w-120pc">

                    <div className="flex justify-around">

                        <div className="w-30pc md-px-10 mb-10">
                            <h3 className="white">项目经理</h3>
                            <br/>
                            <p className="white opacity-80">王思远</p>
                            <br/><br/>
                            <h3 className="white">产品经理</h3><br/>
                            <p className="white opacity-80">令狐浩天</p><br/><br/>
                            <h3 className="white">架构师</h3>
                            <br/>
                            <p className="white opacity-80">林煜轩</p><br/>
                        </div>

                        <div className="w-60pc md-px-10 mb-10">


                            <h3 className="white">后端人员</h3><br/>
                            <p className="white opacity-80">黄宇昂 汤灿辉 陈景行</p><br></br>
                            <h3 className="white">前端人员</h3><br/>
                            <p className="white opacity-80">陈睿阳 陈颖 高天一</p>
                            <h4 className="white fw-600 fs-m2 mt-10">Contact us</h4>

                            <div className="w-100pc md-w-70pc">

                                <div className="flex justify-around my-8">
                                    <a href="#" className="relative p-5 bg-indigo br-round white hover-scale-up-1 ease-400"><svg
                                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" className="feather feather-twitter absolute-center h-4">
                                            <path
                                                d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z">
                                            </path>
                                        </svg></a>
                                    <a href="#" className="relative p-5 bg-indigo br-round white hover-scale-up-1 ease-400"><svg
                                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" className="feather feather-facebook absolute-center h-4">
                                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                                        </svg></a>
                                    <a href="#" className="relative p-5 bg-indigo br-round white hover-scale-up-1 ease-400"><svg
                                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round" className="feather feather-instagram absolute-center h-4">
                                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                                        </svg></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </>
    );
};

export default About_us;