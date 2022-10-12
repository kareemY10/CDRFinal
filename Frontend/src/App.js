// import logo from './logo.svg';
import './Style/App.css';
import React from 'react';
// import HomeNavbar from './components/HomeNavbar';
import HomePage from './components/Home';
import About from './components/About';
import { BrowserRouter as Router, Routes, 
  Route, Navigate,} from "react-router-dom";
import Login from './components/Login';
function App() {
  return (
    <>
      {/* This is the alias of BrowserRouter i.e. Router */}
      <Router>
        <Routes>
          {/* This route is for home component 
          with exact path "/", in component props 
          we passes the imported component*/}
          <Route  path="/home" element={<HomePage/>} />
            
          {/* This route is for Login component 
          with exact path "/", in component props 
          we passes the imported component*/}
          <Route  path="/Login" element={<Login/>} />
          {/* This route is for about component 
          with exact path "/about", in component 
          props we passes the imported component*/}
          <Route path="/about" element={<About/>} />
            

            
          {/* If any route mismatches the upper 
          route endpoints then, redirect triggers 
          and redirects app to home component with to="/" */}
          <Route path="/" element={<Navigate replace to="/home" />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;



    // <div className="App">
    //  <React.StrictMode>
    //   {/* NavBar file: */}
    //   <HomeNavbar />
    //   {/* Home page file: */}
    //   <HomePage />
    //   {/* The about div:- */}
    //   <About />
    // </React.StrictMode>
    // </div>