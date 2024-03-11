import { useState } from 'react'

const Attribute = ({ value }) => {
    const [inRevision, setInRevision] = useState(false);
    const [input, setInput] = useState(value);

    const handleClick = () => {
        setInRevision(true);
    }

    const handleChange = (event) => {
        setInput(event.target.value)
    }
    const handleBlur = () => {
        setInRevision(false);
    }

    return (
        <div onClick={handleClick}>
            {
                inRevision ? (
                    <input value={input} onChange={handleChange} onBlur={handleBlur} onSubmit={handleBlur} />) : (
                    <span>{input}</span>
                )

            }
        </div>
    )

}

export default Attribute;