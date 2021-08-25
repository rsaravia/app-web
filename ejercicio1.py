# 1. Create a simple function that fetches and parses the JSON from this API:
# a. https://jsonplaceholder.ty.picode.com/todos/ and then print all the completed TODOs in the screen
# b. Create a simple local web server with an API endpoint that proxies the TODOs API used above
#    and accepts the "completed" and the "name" filtering. You can use nay web framework you prefer
import urllib.request
import time
import tempfile
import shutil
import json

url = 'https://jsonplaceholder.typicode.com/todos/'

"""
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = (response.read())
"""

with urllib.request.urlopen(url) as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name, "r") as html:
    data = json.load(html)

total = len(data)
found = 0

for element in data:
    if element["completed"] == True:
        found += 1
        for key,value in element.items():
            print(f"{key} = {value}")
        print("----")

print(f"From {total} elements {found} was found.!!")




