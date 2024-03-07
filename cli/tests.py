#!/usr/bin/env python3

"""
This file tests the functionality of auto resumed the Cli

    *

"""
#imports
import os
import json
from pprint import pprint as pprint

from autoresumed import *

def testParse(js):
    # testing parsing
    pprint("## Parse Test Resume ##")
    pprint(parseResume(js,["tech"]), sort_dicts=False)

def testStripTags(js, tags):
    pprint("## Strip Test ##")
    res = parseResume(js, tags)
    pprint(stripTags(res), sort_dicts=False)
  

def testFlatten(js, tags):
    pprint("## Flaten Test ##")
    pprint(flatenResume(js, tags), sort_dicts=False)

if __name__ == "__main__":
    with open("test.json", 'r') as file:
        js = json.load(file)
        #starting 
        #testParse(js)
        #testStripTags(js, ["tech"])
        testFlatten(js, ["tech"])
