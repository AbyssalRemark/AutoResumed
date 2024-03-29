#!/usr/bin/env python3

"""
This program is used to manipulate monolithic resumeon resumes to generate spesific 
resumes off of taged entries for faster resume making.

    * create defaults
        *  
    * manipulate basics
    * add entries 
    * add tags
    * gen resume off of tags. 

    *resumeon to data structure and back again. 
    *

"""
#imports
import os
import json
from pprint import pprint as pprint
from typing import Final
from copy import deepcopy #python shallow copies by default. 

#const fields for talking about whats in the resume
CONST_FIELDS: Final = ["basics", "work", "volunteer", "education", "awards", "certificates", 
                       "publications", "skills", "languages", "interests", "references", "projects"]

#==============================================================================#
#
#   Resume translating functions
#
#==============================================================================#

# creates a Resume 
def flatten_resume(resume, tags):
    res = parseResume(resume, tags)
    res = stripTags(res)
    return res

#==============================================================================#
#
#   Resume editing and creation
#
#==============================================================================#

def addEntry(resume, field, entry):
    match(field):
        #special cases within basics..
        case "label" | "summary" | "profiles":
            resume["basics"][field].append(entry)

        #All tagged fields
        case "work" | "volunteer" | "education" | "awards" | "certificates" | "publications" | "skills" | "languages" | "interests" | "references" | "projects":
            resume[field].append(entry)
        #Any non tagged fields 

#some notes for myself
#not currently my job but will be later..
#   not responsible for createion...?
#   add
#   update
#      add tags
#      add entrys
#   not responsible for deletion...
#   will need logic to sort by date...?

#def parseResume(resumeon, tags):
#def parseResume returns flatend resume
#def parseList returns relivent parts of list.

#insertion into work history needs to be chronological I think but idk.

#==============================================================================#
#
#   Private things you can use but probably shouldn't
#
#==============================================================================#
#for lists
def parseAll(list, tags): #knowing python this can probasbly be one line but idk
    parsed = [] 
    for i in list:
        for j in tags:
            if j in i["tags"]: #any tag found
                parsed.append(deepcopy(i))
                break
    return parsed

def parseFirst(list, tags):
    for i in list:
        for j in tags:
            if j in i["tags"]: #any tag found
                #same logic as above but returns the first one
                return deepcopy(i)
    #if that doesnt occure look for the special tag default.
    for i in list:
        if "default" in i["tags"]:
            #if this doesnt exist something has gone wrong.
            #TODO throw error I guess
            return append(deepcopy(i))


#assumes its been loaded correctly.
#   Does not remove tags. 
#   Cassidy you probably want genResume not this.
#   *Should* not modify resume in any way
def parseResume(resume, tags):
    #where the new resume goes
    res = {}
    # "education", is not tagged and needs to be pulled seperately. 
    for field in (CONST_FIELDS):
        # "education", is not tagged and needs to be pulled seperately. 
        match(field):
            case "basics":
                #grabs tagged single fields because there special

                #copys all entry to avoid indevidual copying, deep copy
                basics = deepcopy(resume["basics"]) #for easier reading further down
                res["basics"] = basics

                #grabs correct tag (hence why we may need default to be special)
                label = parseFirst(basics["label"], tags)

                summary = parseFirst(basics["summary"], tags)

                #needs to check if we still failed to grab a default
                if label == None:
                    res["basics"]["label"]  = ""
                else:
                    res["basics"]["label"] = label["label"]
                if summary == None:
                    res["basics"]["summary"] = ""
                else:
                    res["basics"]["summary"] = summary["summary"]

                #profiles are not a grab one its a grab all that apply
                res["basics"]["profiles"] = parseAll(basics["profiles"], tags)
            case "work" | "volunteer" | "education" | "awards" | "certificates" | "publications" | "skills" | "languages" | "interests" | "references" | "projects":
                #grabs all tags that apply. 
                #not a fan of all those | but it is correct.
                #print("parse all for " + field)
                res[field] =  parseAll(resume[field], tags)
            case _:
                #default behavior, copy all fields, these are not tagged. None should exist now
                #print("default for " + field)
                res[field] = resume[field]
    return res

def stripTags(resume):
    #sense python flip flops on weather things are passed by value or refference 
    #were not taking any chances with how this is used so we copy it manually
    #just in case to prevent the original from being stripped. 
    res = deepcopy(resume)
    for field in CONST_FIELDS:
        match(field):
            case "basics":
                #basics is special but only a subfield profiles will still have tags
                for profile in res["basics"]["profiles"]:
                    del profile["tags"]
            case "work" | "volunteer" | "education" | "awards" | "certificates" | "publications" | "skills" | "languages" | "interests" | "references" | "projects":
                for entry in res[field]:
                    del entry["tags"]
            #case _:
                #default behavior does nothing. as these are all untagged fields
    return res

if __name__ == "__main__":
    with open("test.resumeon", 'r') as file:
        resume = json.load(file)
    #pprint(resume, sort_dicts=False)
    #print(type(resume))
    #pprint(parseAll(work, ["craft"]))
    #pprint(parseFirst(resume["basics"]["label"],["tech"]))
    #parsed = parseResume(resume,["tech"])
    #pprint(parsed, sort_dicts=False)
    #pprint(stripTags(parsed), sort_dicts=False)
    #pprint(flatenResume(resume, ["tech"]), sort_dicts=False)
    #print("")
    #print("")
    #print("")
    #pprint(flatenResume(resume, ["craft"]), sort_dicts=False)
