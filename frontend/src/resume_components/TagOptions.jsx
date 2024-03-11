import { useContext, useState } from 'react'
import { Form } from 'react-bootstrap'
import { FormContext } from '../Pages/UserForm'
import Tag from './Tag'
const TagOptions = () => {
    const { dummyTags } = useContext(FormContext)
    const [selectedTags, setSelectedTags] = useState(dummyTags);
    const [isChecked, setIsChecked] = useState(true)

    const handleClick = (clickedTag) => {

        if (!selectedTags.includes(clickedTag)) {
            selectedTags.push(clickedTag)
        } else {
            selectedTags.splice(selectedTags.indexOf(clickedTag), 1)
        }
        console.log(selectedTags)
        //setIsChecked(!isChecked)
    }

    const handleChecked = (clickedTag) => {
        if (selectedTags.includes(clickedTag)) {
            return true
        }
        return false
    }

    return (
        <div>
            <Form>
                {
                    dummyTags.map((tag) =>
                        <Tag key={tag} tag={tag} />
                    )
                }
            </Form>
        </div>
    )

}

export default TagOptions;
