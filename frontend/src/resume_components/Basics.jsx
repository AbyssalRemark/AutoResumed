import { useState, useContext, createContext } from 'react';
import { FormContext } from '../Pages/UserForm'
import Entry from './Entry'
import Attribute from './Attribute'

export const BasicsContext = createContext(null)

const Basics = () => {

    const { JSONResume } = useContext(FormContext)
    const entries = Object.keys(JSONResume["basics"])


    // name
    // label
    // image
    // location
    // profiles
    // summary
    // url

    return (
        <div>
            <Attribute value="" />

            {entries.map((entry) =>
                <h1 key={entry}>{(entry != "profiles" && entry != "summary" && entry != "location" && entry != "label") ? JSONResume["basics"][entry] : entry}</h1>
            )}
        </div>
    )
}

export default Basics; 