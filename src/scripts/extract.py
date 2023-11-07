# Script to read text data from lines.txt and organizes it into a dictionary as an output of JSON data for MongoDB
import json
import pathlib

PROJECT_ROOT = f"{pathlib.Path(__file__).parent.resolve()}/../.."

file_lines = []

with open(f'{PROJECT_ROOT}/src/data/lines.txt', 'r') as file:
    file_lines = file.readlines()

d = {
    'lines': []
}

for line in file_lines:
    d['lines'].append(line)

with open(f'{PROJECT_ROOT}/src/data/lines.json', 'w') as file:
    json.dump(d, file)