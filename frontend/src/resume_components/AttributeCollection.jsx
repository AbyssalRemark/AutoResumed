import { Form, Button } from 'react-bootstrap';
import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import { Accordion, AccordionBody } from 'react-bootstrap';
import Attribute from './Attribute'

const AttributeCollection = ({ parentField, parentEntry }) => {
    const { JSONResume } = useContext(FormContext)
    const attributeList = JSONResume[parentField][parentEntry]
    const attributes = Object.keys(attributeList).slice(1, 20);

    console.log(attributes)


    return (
        <div>
            {attributes.map((attribute) =>
                <Attribute label={attribute} value={attributeList[attribute]}></Attribute>
            )}
        </div >
    );
}

export default AttributeCollection;