import { Form, Button } from 'react-bootstrap';
import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import { Accordion, AccordionBody } from 'react-bootstrap';
import Attribute from './Attribute'

const AttributeCollection = ({ parentField, parentEntry }) => {
    const { JSONResume } = useContext(FormContext)
    const attributeList = JSONResume[parentField][parentEntry]
    console.log(attributeList)
    const attributes = Object.keys(attributeList);
    attributes.map((attr, index) => {
        console.log(attr)
    })

    return (
        <div>
            {attributes.map((attribute, index) => {
                <Attribute key={attribute} value={attribute} />
            })}
        </div >
    );
}

export default AttributeCollection;