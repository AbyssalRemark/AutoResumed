
import { redirect, useNavigate } from 'react-router-dom';
import { Form, Button } from 'react-bootstrap';
import { useState } from 'react';
import PreviousButton from './PreviousButton.jsx';
//import axios from 'axios';

const LoginPage = () => {
  const [passwordVisibility, setPasswordVisibility] = useState("password")
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")

  // abc@123.com
  // password

  async function sendLoginRequest(email_input, password_input) {

    //const url = "https://autoresumed.com/auth/login";
    const url = "http://127.0.0.1:5000/auth/login"
    const response = await fetch(url, {
      method: "POST",
      mode: "cors",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json;",
        "Access-Control-Allow-Origin": "*",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify({
        email: "abc@123.com",
        password: "password"
      }),
    });
    return response.json();
  };

  const handleSubmit = event => {
    event.preventDefault();
    if (email != "" && password != "") {
      sendLoginRequest(email, password).then((data) => {
        if (data) {
          console.log(type(data));
        } else {
          console.log("no data");
        }
      });
    } else {
      console.log("Email or password was empty");
    }
  };

  return (

    <div className="info">

      <PreviousButton></PreviousButton>
      <Form>
        <Form.Group className="mb-3" controlId="loginForm.email">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="name@example.com" value={email} onChange={(e) => setEmail(e.target.value)} />
        </Form.Group>

        <Form.Group className="mb-3" controlId="loginForm.password">
          <Form.Label>Example textarea</Form.Label>
          <Form.Control type={passwordVisibility} value={password} onChange={(e) => setPassword(e.target.value)} />
          <Button variant="danger" type="button" onClick={() => setPasswordVisibility(passwordVisibility == "password" ? "textarea" : "password")}>{passwordVisibility == "password" ? "show" : "hide"}</Button>
          <Button variant="success" type="submit" onClick={handleSubmit}>Submit</Button>
        </Form.Group>

      </Form>
    </div>
  );
};

export default LoginPage;
