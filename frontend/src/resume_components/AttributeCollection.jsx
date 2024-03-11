import { Form, Button } from 'react-bootstrap';
import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import { Accordion, AccordionBody } from 'react-bootstrap';
import Attribute from './Attribute'
import TagOptions from './TagOptions'
const AttributeCollection = ({ parentField, parentEntry, isNew }) => {
    const { JSONResume } = useContext(FormContext)

    const attributeList = JSONResume[parentField][parentEntry]
    const attributes = Object.keys(attributeList).slice(1, 20); // Sliced to not include tags. To Do: dropdown or radio box of tags. 

    return (
        <div>
            {isNew ? <TagOptions /> : <></>}

            {attributes.map((attribute) =>
                <Attribute
                    key={attribute}
                    label={attribute}
                    isNew={isNew}
                    value={attributeList[attribute]}></Attribute>
            )}
        </div >
    );
}

export default AttributeCollection;