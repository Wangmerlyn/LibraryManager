import React from "react"
import logo1 from './assets/images/logo1.jpg'
import ant from "./assets/images/ant5.png"
import book from "./assets/images/book3.png"
import tool from "./assets/images/tool4.png"

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



            <section id="features" className="p-10 md-p-l3">

                <div className="flex flex-column md-flex-row mx-auto">
                    <div className="w-100pc md-w-40pc">
                        <div className="br-8 p-5 m-5">
                            <div className="flex justify-center items-center bg-indigo-lightest-10 white w-l7 h-l7 br-round mb-5">


                                <img className="max-h-l5 w-auto" src={ant} />

                            </div>
                            <h4 className="white fw-600 fs-m3 mb-5">Ant Design Pro</h4>
                            <div className="indigo-lightest fw-600 fs-m1 lh-3 opacity-50">Ant design?????????????????????react??????????????????????????????????????????UI?????????
                                ???Ant design pro?????????Ant Design????????????????????????????????????????????????????????????</div>

                        </div>
                    </div>

                    <div className="w-100pc md-w-40pc">
                        <div className="br-8 p-5 m-5">
                            <div className="flex justify-center items-center bg-indigo-lightest-10 white w-l7 h-l7 br-round mb-5">

                                <img className="max-h-l5 w-auto" src={book} />
                            </div>
                            <h4 className="white fw-600 fs-m3 mb-5">??????????????????</h4>
                            <div className="indigo-lightest fw-600 fs-m1 opacity-50">
                                ??????????????????????????????????????????????????????????????????????????????????????????????????????</div>

                        </div>
                    </div>

                    <div className="w-100pc md-w-40pc">
                        <div className="br-8 p-5 m-5">
                            <div className="flex justify-center items-center bg-indigo-lightest-10 white w-l7 h-l7 br-round mb-5">

                                <img className="max-h-l4 w-auto" src={tool} />
                            </div>
                            <h4 className="white fw-600 fs-m3 mb-5">?????????</h4>
                            <div className="indigo-lightest fw-600 fs-m1 opacity-50">Node js ?????????????????????JavaScript</div>
                            <div className="indigo-lightest fw-600 fs-m1 opacity-50">Flask ??????Python??????????????????Web????????????</div>
                            <div className="indigo-lightest fw-600 fs-m1 opacity-50">SQL ???????????????????????????</div>
                            <div className="indigo-lightest fw-600 fs-m1 opacity-50">...</div>
                        </div>
                    </div>
                </div>


            </section>



            </div>
    </>
    );
};

export default About_us;