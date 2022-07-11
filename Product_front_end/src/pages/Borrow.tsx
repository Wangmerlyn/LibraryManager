import logo from "./assets/images/logo1.jpg"

const Borrow: React.FC = () =>{
    return (
        <>
            <head>
                <meta charSet="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
        
                <link rel="stylesheet" href="dist/style.css" />

                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <title>book information</title>

                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/shorthandcss@1.1.1/dist/shorthand.min.css" />

            </head>




            <body className="bg-black muli">


                <nav className="w-100pc flex flex-column md-flex-row md-px-10 py-5 bg-black">
                    <div className="flex justify-between">
                        <a href="#" className="flex items-center p-2 mr-4 no-underline">
                            <img className="max-h-l2 w-auto" src={logo} />
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



                <section className="wrapper">
                    <main className="row title">
                        <ul>
                            <li > Sport </li>
                            <li> Entry $ </li>
                            <li><span className="title-hide">#</span> Entries</li>
                            <li>Max</li>
                            <li>Time</li>
                        </ul>
                    </main>
                    <section className="row-fadeIn-wrapper">
                        <article className="row fadeIn nfl">
                            <ul>
                                <li><a href="#">NFL</a><span className="small">(fadeIn)</span></li>
                                <li>$50</li>
                                <li>12</li>
                                <li>48</li>
                                <li>2:00ET</li>
                            </ul>
                            <ul className="more-content">
                                <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                    positions. First place wins $100,000.00. Good luck!</li>
                            </ul>
                        </article>
                    </section>
                    <section className="row-fadeOut-wrapper">
                        <article className="row nfl">
                            <ul>
                                <li><a href="#">NFL</a><span className="small">(fadeOut)</span></li>
                                <li>$5</li>
                                <li>45</li>
                                <li>100</li>
                                <li>3:00ET</li>
                            </ul>
                            <ul className="more-content">
                                <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                    positions. First place wins $100,000.00. Good luck!</li>
                            </ul>
                        </article>
                    </section>
                    <article className="row nfl">
                        <ul>
                            <li><a href="#">NHL</a></li>
                            <li>$50</li>
                            <li>12</li>
                            <li>48</li>
                            <li>12:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>
                    <article className="row mlb update-row">
                        <ul>
                            <li><a href="#">MLB</a><span className="small">(update)</span></li>
                            <li>$10</li>
                            <li><span className="update1">1</span><span className="update2">2</span></li>
                            <li>10</li>
                            <li>1:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>
                    <article className="row mlb">
                        <ul>
                            <li><a href="#">MLB</a></li>
                            <li>$5</li>
                            <li>48</li>
                            <li>120</li>
                            <li>12:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>
                    <article className="row nhl">
                        <ul>
                            <li><a href="#">NHL</a></li>
                            <li>$50</li>
                            <li>12</li>
                            <li>48</li>
                            <li>12:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>
                    <article className="row nhl">
                        <ul>
                            <li><a href="#">NHL</a></li>
                            <li>$50</li>
                            <li>12</li>
                            <li>48</li>
                            <li>12:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>
                    <article className="row pga">
                        <ul>
                            <li><a href="#">PGA</a></li>
                            <li>$50</li>
                            <li>12</li>
                            <li>48</li>
                            <li>11:00ET</li>
                        </ul>
                        <ul className="more-content">
                            <li>This 1665-player contest boasts a $300,000.00 prize pool and pays out the top 300 finishing
                                positions. First place wins $100,000.00. Good luck!</li>
                        </ul>
                    </article>

                </section>
            </body>
        </>
    );
};

export default Borrow