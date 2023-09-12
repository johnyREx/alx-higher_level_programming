#!/usr/bin/python3
"""
Read json file and create
object
"""


import json


def load_from_json_file(filename):
    """
    Read filename and create object
    """
    with open(filename, 'r') as file:
        return(json.loads(file.read()))
