import HomePic from '../images/HomePage.png';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import '../Style/Home.css'
const width=600;
const height=350;
const HomePage = ()=> {
    return(
        <div id="Home">
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
            <div id="home-image">
              <img src={HomePic} className="center"  width={width} height={height} alt="Email security"/>
                <br></br><br></br>
             </div>
            <div id="Home-par" style={{textAlign: 'left'}} >
                <h2 className='text-primary'>What is Content disarm & reconstruction (CDR)?</h2>
                <p className='fw-light'> 
                    Also known as 'file sanitization' or 'content sanitization' - Content Disarm & Reconstruction (CDR) is an <b>advanced technology providing superior results in the prevention of file-based attacks - effectively blocking the initial access phase of most APT's</b>, <u className='text-danger'>ransomware and zero-day attacks.</u>
                    CDR generates for each incoming email and file, a functionally identical new copy that is devoid of any malicious content or links- transparently, in near real-time.
                    A major benefit of CDR is that it eliminates reliance on user judgement and compliance, since all incoming content is disarmed prior to entry.
                    An added benefit of the technology is the capacity to apply precision data redaction to the outgoing stream, enabling the prevention of data exfiltration or loss, supporting data-protection and privacy policies (GDPR/CCPA) compliance.
                </p>
            </div>
        </div>
    );
}


export default HomePage;