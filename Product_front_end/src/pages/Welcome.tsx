import logo from "./assets/images/logo1.jpg"
import borrow_book_img from "./assets/images/yoann-siloine-dyaxQ-aoGWY-unsplash.jpg"
import return_book_img from "./assets/images/florian-klauer-mk7D-4UCfmg-unsplash.jpg"
import { useAccess, Access, useModel } from "umi";
import { currentUser } from "@/services/ant-design-pro/api";

const Welcome: React.FC = () => {
    const access = useAccess();
    const {initialState } = useModel('@@initialState');
  return (
    <>
      <div className="bg-black muli">
        <nav className="w-100pc flex flex-column md-flex-row md-px-10 py-5 bg-black">
            {/* <Access accessible={access.canAdmin}> */}
            <div  className="flex justify-between">
                <a href="#" className="flex items-center p-2 mr-4 no-underline">
                    <img className="max-h-l2 w-auto" src={logo} />
                </a>
                <a data-toggle="toggle-nav" data-target="#nav-items" href="#"
                    className="flex items-center ml-auto md-hidden indigo-lighter opacity-50 hover-opacity-100 ease-300 p-1 m-3">
                    <i data-feather="menu"></i>
                </a>
            </div>
            {/* </Access> */}
            {/* {access.canAdmin && <div></div>} */}
            <div id="nav-items" className="hidden flex sm-w-100pc flex-column md-flex md-flex-row md-justify-end items-center">
                <a href="../welcome" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Home</a>
                <a href="../features" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Features</a>
                <a href="https://github.com/Wangmerlyn/LibraryManager" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">Github</a>
                <a href="../about_us" className="fs-s1 mx-3 py-3 indigo no-underline hover-underline">About Us</a>

            </div>
        </nav>

        <section className="p-0 md-p-5">
            <div className="flex flex-wrap">

                <div className="w-100pc md-w-40pc p-6">
                    <a href="admin/book"
                        className="block no-underline p-5 br-8 hover-bg-indigo-lightest-10 hover-scale-up-1 ease-300">
                        <img className="w-100pc" src={borrow_book_img} alt="" />
                        <p className="fw-600 white fs-m3 mt-3">借书
                        </p>
                        <div className="indigo fs-s3 italic after-arrow-right my-4">Borrow Books</div>
                    </a>
                </div>

                <div className="w-100pc md-w-40pc p-6">
                    <a href="#" className="block no-underline p-5 br-8 hover-bg-indigo-lightest-10 hover-scale-up-1 ease-300">
                        <img className="w-100pc" src={return_book_img} alt=""/>
                        <p className="fw-600 white fs-m3 mt-3">还书
                        </p>
                        <div className="indigo fs-s3 italic after-arrow-right my-4">Return Books</div>
                    </a>
                </div>

            </div>
        </section>
    </div>
  </>
  );
};

export default Welcome;
