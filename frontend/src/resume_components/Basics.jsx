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
            <Attribute label="name" value={JSONResume["basics"]["name"]} />

            <Attribute label="image" value={JSONResume["basics"]["image"]} />
            <Attribute label="url" value={JSONResume["basics"]["url"]} />
        </div>
    )
}

export default Basics; 