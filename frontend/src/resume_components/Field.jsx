import { useState, useContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import Entry from './Entry'
import NewEntry from './NewEntry'
import Accordion from 'react-bootstrap/Accordion'
import Basics from './Basics'
import { AccordionBody } from 'react-bootstrap';
import { Tab, Tabs } from 'react-bootstrap';

const Field = ({ fieldTitle }) => {
    const { JSONResume } = useContext(FormContext)
    const fields = Object.keys(JSONResume).slice(1, 12)

    return (
        <div>
            <Tabs>
                {
                    fields.map((field) =>
                        <Tab eventKey={field} key={field} title={field}>
                            <Entry parentField={field} />
                        </Tab>)
                }
            </Tabs>
        </div>
    )
    {/*} if (fieldTitle != "basics") {
        const entries = Object.keys(JSONResume[fieldTitle]);
        return (
            <div className={fieldTitle}>
                <style type="text/css">
                    {`
                        .accordion-item:first-of-type > .accordion-header .accordion-butentry {
                            font-style: italic !important;
                        }
                        `}
                </style>
                <Accordion defaultActiveKey="0">
                    {entries.map((entry) =>
                        <Accordion.Item eventKey="0">

                            <Accordion.Header>
                                {entry}
                            </Accordion.Header>
                            <AccordionBody></AccordionBody>

                        </Accordion.Item>)}

                    <Accordion.Item eventKey="1">
                        <Accordion.Header>
                            +
                        </Accordion.Header>
                        <Accordion.Body>
                            {entries.map((entry) =>
                                <NewEntry
                                    label={entry}
                                    key={entry} />)}
                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
            </div>
        );
    } else {
        const basicsEntries = Object.keys(JSONResume["basics"])
        return <div></div>
    }
*/}
}

export default Field;
