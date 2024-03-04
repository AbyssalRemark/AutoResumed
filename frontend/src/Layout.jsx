import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import { Nav, Navbar, NavDropdown, Container, Button } from "react-bootstrap";
import Welcome from "./Welcome.jsx"
import LoginPage from "./LoginPage.jsx"
import RegistrationPage from "./RegistrationPage.jsx"
import UserForm from "./UserForm.jsx";

import 'bootstrap/dist/css/bootstrap.css';

const Layout = () => {
  /*return (
<BrowserRouter>
  <h1>AutoResumed</h1>
  <Link to="/login">login</Link>
  {` `}
  <Link to="/register">register</Link>
  <Routes>
    <Route path="/" element={<Layout />} />
    <Route path="/login" element={<LoginPage />} />
    <Route path="/register" element={<RegistrationPage />} />
  </Routes>
</BrowserRouter>
  );*/
  return (
    <div>
      <style type="text/css">
        {`
    body {
      background-color: rgb(255, 241, 143);
    }

    .bg-body-tertiary{
        color: blue;
        background-color: white !important;
    }
    `}</style>

      <Navbar expand="lg" className="bg-body-tertiary" >
        <Container>
          <Nav fill variant="tabs" defaultActiveKey={"/"}>
            <h1>Autoresumed</h1>
            <Nav.Item>
              <Link to="/login"><Button variant="outline-danger">login</Button></Link>
            </Nav.Item>
            {` `}
            <Nav.Item>
              <Link to="/register"><Button variant="outline-danger">register</Button></Link>
            </Nav.Item>


            <Nav.Item>
              <Link to="/create"><Button variant="outline-danger">create</Button></Link>
            </Nav.Item>
          </Nav>
        </Container>

      </Navbar>
    </div>
  );
};

export default Layout