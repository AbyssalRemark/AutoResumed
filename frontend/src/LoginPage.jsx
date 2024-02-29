import {Form, Button} from 'react-bootstrap';
import { useState } from 'react';
import PreviousButton from './PreviousButton.jsx';

const LoginPage = () => {
    const [passwordVisibility, setPasswordVisibility] = useState("password")

    return (

      <div className="info">
        
        <PreviousButton></PreviousButton>
        <Form>
      <Form.Group className="mb-3" controlId="loginForm.email">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="name@example.com" />
      </Form.Group>
      
      <Form.Group className="mb-3" controlId="loginForm.password">
        <Form.Label>Example textarea</Form.Label>
        <Form.Control type={passwordVisibility}/>
        <Button variant="danger" type="button" onClick={()=>setPasswordVisibility(passwordVisibility=="password" ? "textarea" : "password")}>{passwordVisibility=="password" ? "show" : "hide"}</Button>
      </Form.Group>
    
    </Form>
      </div>
    );
  };
  
  export default LoginPage;