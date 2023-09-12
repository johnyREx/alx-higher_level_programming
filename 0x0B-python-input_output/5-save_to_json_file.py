#!/usr/bin/python3
"""
Converts to json and
saves to file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Converts my_obj to filename and
    saves it in filename
    """
    with open(filename, 'w+') as file:
        file.write(json.dumps(my_obj))
