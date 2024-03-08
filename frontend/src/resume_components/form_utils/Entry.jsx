import { Form } from 'react-bootstrap';
import { useState } from 'react';
const Entry = ({ label }) => {
    const [input, setInput] = useState("")

    return (
        <div className={label}>
            <Form>
                <Form.Group className="mb-3" controlId={label}>

                    <Form.Label>{label != "tags" ? label : ""}</Form.Label>
                    <Form.Control placeholder={label} value={input} onChange={(e) => setInput(e.target.value)} />

                </Form.Group>
            </Form>

        </div>
    );
}

export default Entry;