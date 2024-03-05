import { Form, Button } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import PreviousButton from './PreviousButton.jsx';
import Award from './resume_components/Award.jsx';
import Accordion from 'react-bootstrap/Accordion';

const UserForm = () => {

  useEffect(() => {
    console.log("TO-DO: Fetch Edit Page")
      , []
  });



  return (

    <div>
      <Accordion defaultActiveKey="0">
        <Accordion.Item eventKey="0">

          <Accordion.Header>Awards</Accordion.Header>
          <Accordion.Body>
            <Award></Award>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </div>
  );
};

export default UserForm;