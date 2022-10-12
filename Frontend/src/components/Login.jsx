import React from 'react';
import {MDBContainer, MDBCol, MDBRow, MDBBtn, MDBIcon, MDBInput, MDBCheckbox } from 'mdb-react-ui-kit';
import '../Style/Login.css'
import LoginPic from '../images/My_Login.png'


import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


function Login() {

  return (
    <MDBContainer fluid className="p-3 my-3 h-custom">
        <Navbar bg="light" variant="light">
                <Container>
                  <Navbar.Brand href="/home">CDR</Navbar.Brand>
                  <Nav className="me-auto">
                    <Nav.Link href="/home">Home</Nav.Link>
                    <Nav.Link href="#features">Features</Nav.Link>
                    <Nav.Link href="/Login">Login</Nav.Link>
                  </Nav>
                  <Nav clasName="ms-auto">
                    <Nav.Link href="/About">About us</Nav.Link>
                  </Nav>
                </Container>
          </Navbar>
      <MDBRow>

        <MDBCol col='10' md='6'>
          <img src={LoginPic} class="img-fluid" alt="Login" />
        </MDBCol>

        <MDBCol col='4' md='6'>

          <div className="d-flex flex-row align-items-center justify-content-center">

            <p className="lead fw-normal mb-0 me-3"><b>Sign in</b></p>

          

          </div>

          <div className="divider d-flex align-items-center my-4">
          </div>

          <MDBInput wrapperClass='mb-4' label='Email address' id='formControlLg' type='email' size="lg"/>
          <MDBInput wrapperClass='mb-4' label='Password' id='formControlLg' type='password' size="lg"/>

          <div className="d-flex justify-content-between mb-4">
            <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Remember me' />
            <a href="!#">Forgot password?</a>
          </div>

          <div className='text-center text-md-start mt-4 pt-2'>
            <MDBBtn id="LoginButton" className="mb-0 px-5" size='lg'>Login</MDBBtn>
          </div>

        </MDBCol>

      </MDBRow>

      

    </MDBContainer>
  );
}

export default Login;