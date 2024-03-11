import { useState } from 'react'

const Attribute = ({ label, value }) => {
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
            <span>{label}: </span>
            {
                inRevision ? (
                    <input
                        value={input}
                        onChange={handleChange}
                        onBlur={handleBlur}
                        onSubmit={handleBlur}
                        type={label.toLowerCase().includes("date") ? "date" : "text"}
                    />)
                    :
                    (<span>
                        {input}
                    </span>)

            }
        </div>
    )

}

export default Attribute;