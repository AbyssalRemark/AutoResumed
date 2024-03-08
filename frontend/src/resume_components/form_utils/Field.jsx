import { useState, useContext } from 'react';
import { FormContext } from '../../UserForm'
import Entry from './Entry'

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
    console.log(fieldTitle)
    console.log(JSONResume[fieldTitle][0])
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

    if (fieldTitle != "basics") {
        const hello = Object.keys(JSONResume[fieldTitle][0])
        return (
            <div className={fieldTitle}>
                {hello.map((ton) => <Entry label={ton}></Entry>)}
            </div>
        );
    } else {
        return <div>hello!</div>
    }

}

export default Field;
