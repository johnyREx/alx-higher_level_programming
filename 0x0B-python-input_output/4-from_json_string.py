#!/usr/bin/python3
"""
Converts from json
to object
"""


import json


def from_json_string(mystr):
    """
    Converts mystr
    """
    return(json.loads(mystr))
