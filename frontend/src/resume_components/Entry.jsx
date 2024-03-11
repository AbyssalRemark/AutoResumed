import { Form, Button } from 'react-bootstrap';
import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import { Accordion, AccordionBody } from 'react-bootstrap';
import AttributeCollection from './AttributeCollection'
const Entry = ({ parentField }) => {


    const { JSONResume } = useContext(FormContext)
    // tagType

    //  inRevision
    const entryList = JSONResume[parentField]
    const entries = Object.keys(entryList);
    const firstAttributes = entries.map(entry =>
        Object.keys(entryList[entry])[1]
    )
    return (
        <Accordion defaultActiveKey="0">
            {entries.map((entry, index) =>
                <Accordion.Item eventKey="0" key={index}>
                    <Accordion.Header>{entryList[entry][firstAttributes[index]]}</Accordion.Header>
                    <AccordionBody>
                        <AttributeCollection

                            parentField={parentField}
                            parentEntry={entry}
                        />
                    </AccordionBody>
                </Accordion.Item>)
            }
        </Accordion>
    );
}

export default Entry;