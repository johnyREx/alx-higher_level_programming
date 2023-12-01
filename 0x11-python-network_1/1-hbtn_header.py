#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

# Check if a URL is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Get the value of the reqyest id variable from the header
        x_request_id = response.getheader('X-Request-Id')

        # Displlay the value of the requested id variable
        print("X-Request-Id:", x_request_id)

except urllib.error.URLError as e:
    print("Error fetching the URL:", e)
