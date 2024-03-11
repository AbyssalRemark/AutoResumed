import { Form, Button } from 'react-bootstrap';
import { useState } from 'react';
import PreviousButton from '../Utils/PreviousButton.jsx';

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

  async function sendLoginRequest(email_input, password_input) {


    //const url = "https://autoresumed.com/auth/login";
    const url = "http://127.0.0.1:5000/auth/register"
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
        "email": "abc@123.com",
        "password": "password"
      }),
    });
    return response.json();
  };

  const handleSubmit = event => {
    event.preventDefault();
    if ("" == "") {
      sendLoginRequest("example@example.com", "password").then((data) => {
        console.log(data);
      });
    } else {
      console.log("Email or password was empty");
    }
  };

  return (

    <div className="info">
      <Form>

        <Form.Group className="mb-3" controlId="regForm.email">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="name@example.com" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="regForm.password">
          <Form.Label>password</Form.Label>
          <Form.Control type={passwordVisibility} value={input} onInput={handleInput} />
        </Form.Group>


        <Form.Group className="mb-3" controlId="regForm.passwordConfirmation">
          <Form.Label>confirm password</Form.Label>
          <Form.Control type={passwordVisibility} value={confirmationInput} onInput={handleConfirmationInput} />

          {passwordMatch ? "" : "PASSWORDS DO NOT MATCH"}

          <Button variant="danger" type="button" onClick={() => setPasswordVisibility(passwordVisibility == "password" ? "textarea" : "password")}>{passwordVisibility == "password" ? "show" : "hide"}</Button>
          <Button type="submit" onClick={handleSubmit}>Submit</Button>
        </Form.Group>

      </Form>
    </div>
  );
};

export default RegistrationPage;