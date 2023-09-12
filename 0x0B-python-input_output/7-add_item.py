#!/usr/bin/python3
"""
Load list obj
add element to list
Save the list
"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    with open(filename, 'w+'):
        obj = []
finally:
    for item in sys.argv[1:]:
        obj.append(item)
    save_to_json_file(obj, filename)
