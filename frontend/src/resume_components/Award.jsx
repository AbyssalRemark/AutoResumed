import { useState } from 'react'
import { Form, Button } from 'react-bootstrap';
import Entry from './form_utils/Entry';

const Award = () => {
    const [tags, setTags] = useState([]);
    const [title, setTitle] = useState("");
    const [date, setDate] = useState("");
    const [awarder, setAwarder] = useState("");
    const [summary, setSummary] = useState("");

    const [input, setInput] = useState("");

    const placeholder = "hello"
    const label = "label"
    const controlId = "control"

    return (
        <div className="award">
            <Form>
                <h1>Awards</h1>
                <Entry label="tags" placeholder="frontend, backend" controlId="award.tags"></Entry>
                <Entry label="name" placeholder="" controlId="award.name"></Entry>
                <Entry label="date" placeholder="" controlId="award.date"></Entry>
                <Entry label="issuer" placeholder="" controlId="award.issuer"></Entry>
                <Entry label="url" placeholder="" controlId="award.url"></Entry>
            </Form>
        </div>
    )
}

export default Award;