import { Tab, Tabs } from 'react-bootstrap';
import { useState, useEffect, createContext } from 'react';
import tagged from '../../../tagged-resume.json';
import Field from '../resume_components/Field'
import Basics from '../resume_components/Basics'
export const FormContext = createContext(null)

const UserForm = () => {

  async function getResume() {
    const url = "http://127.0.0.1:5000/resume/get"
    const response = await fetch(url, {
      method: "POST",
      mode: "cors",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json;",
        "Access-Control-Allow-Origin": "*",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify({
        token: "386917202016bd08716f9fa2eedf640cb9997fce9979d326a3a9bdc6c15d3f87"
      }),
    });
    return response.json();
  };

  useEffect(() => {
    getResume().then((data) => {
      if (data) {
        console.log(type(data));
      }
    })
  }
    , [])

  // Variables shared via context
  const [JSONResume, setJSONReusme] = useState(tagged);
  const [allTags, setAllTags] = useState([]);
  const [currentTags, setCurrentTags] = useState([]);

  const fields = Object.keys(tagged);

  const dummyTags = ["default", "frontend", "backend", "historical automobiles", "1-tragic clowns"]


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





  return (

    <div>
      <FormContext.Provider value={{
        allTags, setAllTags,
        currentTags, setCurrentTags,
        JSONResume, setJSONReusme,
        dummyTags
      }}>

        <Basics />
        <Field />

      </FormContext.Provider>

    </div>
  )
};

export default UserForm;