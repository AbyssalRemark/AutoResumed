import { Form, Button } from 'react-bootstrap';
import { useState } from 'react';
const Entry = ({ label, value }) => {



    const [input, setInput] = useState("")

    const handleClick = (e) => {
        console.log(input)
    }


    if (label != "tags") {
        return (
            <div className={label}>
                {label} : {value}
            </div>
        );
    } else return (
        <></>
    )
}

export default Entry;