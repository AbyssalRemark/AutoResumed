import {Form, Button} from 'react-bootstrap';
import { useState } from 'react';
import PreviousButton from './PreviousButton.jsx';

const UserForm = ({ label, controlId, placeholder}) => {

    return (

      <div>
   <Form>
      <Form.Group className="mb-3" controlId={controlId}>
        <Form.Label>{label}</Form.Label>
        <Form.Control type="text" placeholder={placeholder} />
      </Form.Group>
    </Form>
      </div>
    );
  };
  
  export default UserForm;