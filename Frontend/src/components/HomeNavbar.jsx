import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
//don't use this file...


const  HomeNavbar = ()=>  {
  return (
    <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="/home">CDR</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="/Login">Login</Nav.Link>
          </Nav>
          <Nav clasName="ms-auto">
            <Nav.Link href="#About">About us</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
  );
}


export default HomeNavbar;