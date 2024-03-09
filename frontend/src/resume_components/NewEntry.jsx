import { Form, Button } from 'react-bootstrap';
import { useState } from 'react';
import TagOptions from './TagOptions'

const NewEntry = ({ label }) => {

    const [input, setInput] = useState("")

    const handleClick = (e) => {
        console.log(input)
    }

    if (label != "tags") {
        return (
            <div className={label}>

                <Form>
                    <Form.Group className="mb-3" controlId={label}>

                        <Form.Label>{label != "tags" ? label : ""}</Form.Label>
                        <Form.Control placeholder={label} value={input} onChange={(e) => setInput(e.target.value)} />
                        <Button onClick={handleClick}>+</Button>

                    </Form.Group>
                </Form>

            </div>
        );
    } else return (
        <TagOptions></TagOptions>
    )
}

export default NewEntry;