import { Tab, Tabs } from 'react-bootstrap';
import { useState, useEffect, createContext } from 'react';
import PreviousButton from './PreviousButton.jsx';
import Award from './resume_components/Award.jsx';
import Accordion from 'react-bootstrap/Accordion';
import tagged from '../../tagged-resume.json';
import Field from './resume_components/form_utils/Field'


export const FormContext = createContext(null)

const UserForm = () => {
  console.log(Object.keys(tagged));

  // Variables shared via context
  const [JSONResume, setJSONReusme] = useState(tagged);
  const [allTags, setAllTags] = useState([]);
  const [currentTags, setCurrentTags] = useState([]);

  const fields = Object.keys(tagged);

  const mapFields = () => {

  }


  // tabbed items Frields
  // useState Order
  // field contains tag options ? tagOptions.map(() => {radioButton} + none + newTag) : none + newTag
  //  if globalTag == "", globalTag = "default"
  // if globalTag == "untagged" - prompt for tag


  // Accordian items Entries
  // entryName contains dates ? entryType = date : entryType = text 
  // parentNode = useState(props.parentNode)
  // on + button clicked, () => {parse JSON, find entry by parent + node name, update global context json}

  // DO NOT SEND BACK NULL

  useEffect(() => {
    console.log("TO-DO: Fetch Edit Page")
      , []
  });

  return (

    <div>
      <FormContext.Provider value={{
        allTags, setAllTags,
        currentTags, setCurrentTags,
        JSONResume, setJSONReusme
      }}>
        <Tabs>
          {fields.map((field) =>
            <Tab eventKey={field} key={field} title={field}>
              <Field fieldTitle={field}></Field>
            </Tab>)}
        </Tabs>

      </FormContext.Provider>

    </div>
  )
};

export default UserForm;