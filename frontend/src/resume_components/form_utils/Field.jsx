import { useState, useContext } from 'react';
import { FormContext } from '../../UserForm'
import Entry from './Entry'
import NewEntry from './NewEntry'
import Accordion from 'react-bootstrap/Accordion'

const Field = ({ fieldTitle }) => {

    //const entries, setEntries =
    // const entries, setEntries = useState({returnEntries})
    // const mapEntries = () => { if last/edited = < Form>< Form>}
    // consts tags = tags if tags, else 

    // const mapTagOptions = () => { allTags; if currentTags  type= checked }
    // onChecked ---> send checked + newlyChcked (name, checked) post req to server, parse return, setChecked, setJSON, setEntries
    // onUnchecked ---> setChecked(...checked - unchecked), setJSON(parent:[newList]

    // {mapTagOptions}
    const { JSONResume } = useContext(FormContext)
    //const { JSONResume, setJSONResume } = useContext(FormContext);
    //console.log(JSONResume[fieldTitle])

    const [entries, setEntries] = useState(Object.keys(JSONResume[fieldTitle]))

    const mapEntries = () => {

        < h1 >

        </h1 >
        /*
        for (let i = 0; i < entries.length; i++) {
            console.log(entries[i][i])
        }
        return <h1>hi</h1>>
        // <Entry>new</Entry>
    */
    }
    const accheaderstyle = () => {
        color: green;
    }

    if (fieldTitle != "basics") {
        const hello = Object.keys(JSONResume[fieldTitle][0])
        return (
            <div className={fieldTitle}>
                <style type="text/css">
                    {`
                        .accordion-item:first-of-type > .accordion-header .accordion-button {
                            font-style: italic !important;
                        }
                        `}
                </style>

                <Accordion>
                    <Accordion.Item>
                        <Accordion.Header>
                            {JSONResume[fieldTitle][0][hello[1]]}
                        </Accordion.Header>
                        <Accordion.Body>
                            {hello.map((ton) => <Entry key={ton} label={ton} value={JSONResume[fieldTitle][0][ton]}></Entry>)}
                        </Accordion.Body>
                    </Accordion.Item>


                    <Accordion.Item>
                        <Accordion.Header>
                            +
                        </Accordion.Header>
                        <Accordion.Body>
                            {hello.map((ton) => <NewEntry label={ton} key={ton}></NewEntry>)}
                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
            </div>
        );
    } else {
        return <div>hello!</div>
    }

}

export default Field;
