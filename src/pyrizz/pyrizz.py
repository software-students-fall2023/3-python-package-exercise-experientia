from pymongo import MongoClient
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))

# Checks if the connection has been made, else make an error printout
try:
    client.admin.command('ping')          
    database = client[os.getenv('MONGO_DBNAME')]          
    print('* Connected to MongoDB!')         

except Exception as err:
    print('* "Failed to connect to MongoDB at', os.getenv('MONGO_URI'))
    print('Database connection error:', err) 

collection = database['lines']

def get_random_line() -> None:
    size = len(collection.find_one({})["lines"])
    random_number = randint(0, size - 1)

    line = collection.find_one({})["lines"][random_number]

    print(line)