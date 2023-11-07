# Script which extracts the pickup lines from the JSON extracted file and inserts it into the MongoDB database. 

from pymongo import MongoClient
import os
from dotenv import load_dotenv 
import json
import pathlib

load_dotenv()

PROJECT_ROOT = f"{pathlib.Path(__file__).parent.resolve()}/../.."

# Establish a database connection with the MONGO_URI (MongoDB Atlas connection)
client = MongoClient(os.getenv('MONGO_URI'))

# Checks if the connection has been made, else make an error printout
try:
    client.admin.command('ping')          
    database = client[os.getenv('MONGO_DBNAME')]          
    print('* Connected to MongoDB!')         

except Exception as err:
    print('* "Failed to connect to MongoDB at', os.getenv('MONGO_URI'))
    print('Database connection error:', err) 

lines = []

with open(f'{PROJECT_ROOT}/src/data/lines.json', 'r') as file:
    data = json.load(file)
    lines = data['lines']

collection = database['lines']

collection.insert_one({
    'lines': lines
})

client.close()