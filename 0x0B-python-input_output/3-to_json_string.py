#!/usr/bin/python3
"""
Converts object to json
Uses json
"""

import json


def to_json_string(myobj):
    """
    Convert myobj to json
    """
    return(json.dumps(myobj))
