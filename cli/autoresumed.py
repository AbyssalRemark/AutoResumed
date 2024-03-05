#!/usr/bin/env python3

"""
This program is used to manipulate monolithic json resumes to generate spesific 
resumes off of taged entries for faster resume making.

    * create defaults
        *  
    * manipulate basics
    * add entries 
    * add tags
    * gen resume off of tags. 

    *json to data structure and back again. 
    *

"""
#imports
import os
import json
from pprint import pprint as pprint

#not responsible for createion...?
#add
#update
#   add tags
#   add entrys
#not responsible for deletion...
#will need logic to sort by date...

#def parseResume(json, tags):
#def parseResume returns flatend resume
#def parseList returns relivent parts of list.

#insertion into work history needs to be chronological I think but idk.

#for lists
def parseAll(list, tags): #knowing python this can probasbly be one line but idk
    parsed = [] 
    for i in list:
        for j in tags:
            if j in i["tags"]: #any tag found
                parsed.append(i)
    return parsed

def parseFirst(list, tags):
    parsed = [] 
    for i in list:
        for j in tags:
            if j in i["tags"]: #any tag found
                parsed.append(i)
                break #same logic as above but returns the first one
    return parsed

#assumes its been loaded correctly. (this can be changed)
def parseResume(js, tags):
    res = {}
    # "education", is not tagged and needs to be pulled seperately. 
    fields = ["basics", "work", "volunteer", "education", "awards", "certificates", 
              "publications", "skills", "languages", "interests", "references", "projects"]

    for field in (fields):
        match(field):
            case "basics":
                #grabs tagged single fields because there special

                #copys all entry to avoid indevidual copying
                basics = js["basics"] #for easier reading further down
                res["basics"] = basics

                #grabs correct tag (hence why we may need default to be special)
                label = parseFirst(basics["label"], tags)
                summary = parseFirst(basics["summary"], tags)

                #label and summary is an list (of size 1) of dicts, so, we look and ask it for the label field
                res["basics"]["label"] = label[0]["label"]
                res["basics"]["summary"] = summary[0]["summary"]

                #profiles are not a grab one its a grab all that apply
                res["basics"]["profiles"] = parseAll(basics["profiles"], tags)

            case "work" | "volunteer" | "awards" | "certificates" | "publications" | "skills" | "languages" | "interests" | "references" | "projects":
                #grabs all tags that apply. 
                print("parse all for " + field)
                res[field] =  parseAll(js[field], tags)
            case _:
                #default behavior, copy all fields, these are not tagged.
                print("default for " + field)
                res[field] = js[field]
    return res

if __name__ == "__main__":
    with open("test.json", 'r') as file:
        js = json.load(file)
    #pprint(js, sort_dicts=False)
    #print(type(js))

    work = js["work"]
    #pprint(parseAll(work, ["craft"]))
    #pprint(parseFirst(js["basics"]["label"],["tech"]))
    pprint(parseResume(js,["tech"]), sort_dicts=False)
