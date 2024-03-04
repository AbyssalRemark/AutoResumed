import { Form } from 'react-bootstrap';
import { useState } from 'react';
const Entry = ({ label, controlId, placeholder }) => {
    const [input, setInput] = useState("")

    return (
        <div className={controlId}>
            <Form.Group className="mb-3" controlId={controlId}>

                <Form.Label>{label}</Form.Label>
                <Form.Control placeholder={placeholder} value={input} onChange={(e) => setInput(e.target.value)} />

            </Form.Group>
        </div>
    );
}

export default Entry;