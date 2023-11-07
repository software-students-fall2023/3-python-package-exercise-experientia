import os
from random import randint
import pathlib
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import openai

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
openai.api_key = os.getenv('OPENAI_API_KEY')
PROJECT_ROOT = f"{pathlib.Path(__file__).parent.resolve()}/../.."

# Checks if the connection has been made, else make an error printout
try:
    client.admin.command('ping')          
    database = client[os.getenv('MONGO_DBNAME')]          
    print('*****') 

except Exception as err:
    print('* "Failed to connect to MongoDB at', os.getenv('MONGO_URI'))
    print('Database connection error:', err) 

collection = database['dev_lines']

def get_random_line() -> None:
    size = len(collection.find_one({})["lines"])
    random_number = randint(0, size - 1)

    line = collection.find_one({})["lines"][random_number]

    print(line)

def get_random_categorized_line() -> None:
    print("testing")

def get_ai_line(category) -> str:
    # response = openai.ChatCompletion.create(
    #     model = os.getenv('OPENAI_MODEL'),
    #     messages =
    #         [{"role": "user", "content": f"I need a {category} pick-up line."},]
    # )

    # message = response.choices[0]['message']
    # ai_line = "{}".format(message['content'])

    collection = database['ai_generated']

    lines = collection.find_one({})["lines"]
    print(lines)
    
    # lines.append(ai_line)

    # collection.insert_one({
    #     'lines': lines
    # })

    # return ai_line
    return 'testing'

def add_user_line():
    templates_file_path = PROJECT_ROOT + '/src/data/templates.json'

    try:
        with open(templates_file_path, 'r', encoding='utf-8') as file:
            templates = json.load(file)["templates"]
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except FileNotFoundError:
        print(f"The file {templates_file_path} was not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    print("Choose a template number (1-20):")
    try:
        template_number = int(input("> ")) - 1  
        if not (0 <= template_number < len(templates)):
            print("Template number out of range. Please choose between 1 and 20.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    template_to_show = templates[template_number]
    placeholders_count = template_to_show.count("{}")  
    placeholder_representation = ['______'] * placeholders_count 
    print("Fill in the blanks for the following template:")
    print(template_to_show.format(*placeholder_representation))

    print(f"Enter {placeholders_count} word(s) separated by a comma to fill into the template:")
    words = input("> ").split(',')
    words = [word.strip() for word in words] 

    try:
        user_line = templates[template_number].format(*words)
    except IndexError:
        print("Not enough words provided for the placeholders.")
        return
    except Exception as e:
        print(f"An unexpected formatting error occurred: {e}")
        return
    
    if is_line_valid(user_line): 
        try:
            collection = database['user_lines']
            insert_result = collection.insert_one({'line': user_line})
            
            if insert_result.inserted_id:
                print("Here's your custom pick-up line:")
                print(user_line)
                print("Line added to the database successfully!")
            else:
                print("Failed to add line to the database.")
            
        except Exception as e:
            print(f"An error occurred while inserting the line into the database: {e}")
    else: 
        print("Your pick-up line doesn't pass our checks.")

def is_line_valid(user_line):
    if len(user_line) > 140:
        print("Your pick-up line is too long.")
        return False

    if is_offensive(user_line):
        print("Your pick-up line may be offensive.")
        return False
    
    return True

def is_offensive(text):
    try:
        response = openai.Completion.create(
            model="content-filter-alpha",
            prompt="<|endoftext|>"+text+"\n--\nLabel:", 
            temperature=0,  
            max_tokens=1 
        )
        content_filter_response = response["choices"][0]["text"].strip()

        if content_filter_response in ("2", "1"):  
            return True
        else:
            return False
    except openai.error.OpenAIError as e:
        print(f"OpenAIError occurred: {e}")
        return False 
    except Exception as e:
        print(f"An unexpected error occurred when checking for offensive content: {e}")
        return False


