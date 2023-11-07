from pymongo import MongoClient
import os
from dotenv import load_dotenv
from random import randint
import openai

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
openai.api_key = os.getenv('OPENAI_API_KEY')

# Checks if the connection has been made, else make an error printout
try:
    client.admin.command('ping')          
    database = client[os.getenv('MONGO_DBNAME')]          
    print('*****')         

except Exception as err:
    print('* "Failed to connect to MongoDB at', os.getenv('MONGO_URI'))
    print('Database connection error:', err) 

collection = database['lines']

def get_random_line() -> None:
    size = len(collection.find_one({})["lines"])
    random_number = randint(0, size - 1)

    line = collection.find_one({})["lines"][random_number]

    print(line)

def get_random_categorized_line() -> None:
    print("testing")

def get_ai_line(category) -> str:
    response = openai.ChatCompletion.create(
        model = os.getenv('OPENAI_MODEL'),
        messages =
            [{"role": "user", "content": f"I need a {category} pick-up line."},]
    )

    message = response.choices[0]['message']
    ai_line = "{}".format(message['content'])

    collection = database['ai_generated']

    lines = collection.find_one({})["lines"]
    
    lines.append(ai_line)

    collection.insert_one({
        'lines': lines
    })

    return ai_line