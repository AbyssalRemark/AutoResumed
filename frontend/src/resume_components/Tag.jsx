// To-do: tag checked or unchaecked.
// To-do: useContext setTagged to setTag state globally.
import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import { Form } from 'react-bootstrap'

const Tag = ({ tag }) => {

    const { dummyTags } = useContext(FormContext)
    const [selectedTags, setSelectedTags] = useState(dummyTags);
    const [isChecked, setIsChecked] = useState(false)

    return (
        <div>
            <Form.Check key={tag} id={tag} type="checkbox" label={tag} onChange={() => handleClick(tag)} />
        </div>
    );
}

export default Tag;