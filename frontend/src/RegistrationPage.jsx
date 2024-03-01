import {Form, Button} from 'react-bootstrap';
import { useState } from 'react';
import PreviousButton from './PreviousButton.jsx';
import UserForm from './UserForm.jsx';

const RegistrationPage = () => {
  const [passwordVisibility, setPasswordVisibility] = useState("password")
  const [input, setInput] = useState("")
  const [confirmationInput, setConfirmationInput] = useState("")
  const [passwordMatch, setPasswordMatch] = useState(true)

  const handleInput = (e) => {
    setInput(e.target.value);
  }

  const handleConfirmationInput = (e) => {
    setConfirmationInput(e.target.value);
  }

    return (

      <div className="info">
        <PreviousButton></PreviousButton>
        <UserForm label="first name" controlId="regForm.firstName" placeholder="Otto"></UserForm>
        <UserForm label="last name" controlId="regForm.lastName" placeholder="Resumed"></UserForm>
        <Form>

      <Form.Group className="mb-3" controlId="regForm.email">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="name@example.com" />
      </Form.Group>
      
      <Form.Group className="mb-3" controlId="regForm.password">
        <Form.Label>password</Form.Label>
        <Form.Control type={passwordVisibility} value={input} onInput={handleInput}/>
        </Form.Group>  


        <Form.Group className="mb-3" controlId="regForm.passwordConfirmation">
        <Form.Label>confirm password</Form.Label>
        <Form.Control type={passwordVisibility} value={confirmationInput} onInput={handleConfirmationInput}/>
        
        { passwordMatch ? "" : "PASSWORDS DO NOT MATCH"}
        <Button variant="danger" type="button" onClick={()=>setPasswordVisibility(passwordVisibility=="password" ? "textarea" : "password")}>{passwordVisibility=="password" ? "show" : "hide"}</Button>
      </Form.Group>
    
    </Form>
      </div>
    );
  };
  
  export default RegistrationPage;