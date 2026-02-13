import json
import os

def read_json(filename):
    base_path = os.path.dirname(os.path.dirname(__file__))  # go to project root
    file_path = os.path.join(base_path, "testdata", filename)

    with open(file_path, "r") as file:
        return json.load(file)