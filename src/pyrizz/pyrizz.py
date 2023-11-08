import os
import random
import pathlib
import json
from dotenv import load_dotenv
import openai
from pyrizz.pickuplines import pickuplines, user_templates

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_lines(category='all'): 
    if category not in pickuplines:
        print("Category does not exist!")
        return

    else: 
        return pickuplines[category]

def get_random_line(): 
    allpickuplines = get_lines('all')
    return random.choice(allpickuplines)

def get_random_category_line(category='all'):
    category_pickupline = get_lines(category)
    return random.choice(category_pickupline)

def get_ai_line(category) -> str:
    try:
        if (category != "" and len(category) <= 50):
            response = openai.ChatCompletion.create(
                model = os.getenv('OPENAI_MODEL'),
                messages =
                    [{"role": "user", "content": f"I need a {category} pick-up line."},]
            )

            message = response.choices[0]['message']
            ai_line = "{}".format(message['content'])
            return ai_line
        
        elif (category != "" and len(category) > 50):
            return "Please specify a category that is less than 50 characters."
        
        else:
            return "Please specify a category."
            
    except Exception as err:
        return str(err)

def rate_line(pickup_line) -> str:
    try:
        if (pickup_line != ""):
            response = openai.ChatCompletion.create(
                model = os.getenv('OPENAI_MODEL'),
                messages =
                    [{"role": "user", "content": f"Rate this pickup line out of 10: {pickup_line} In your response, STRICTLY follow the format of (nothing else): rating/10 - snazzy comment."},]
            )

            message = response.choices[0]['message']
            ai_rating_response = "{}".format(message['content'])
            return ai_rating_response
        
        else:
            return "No pickup line? You gotta use our other features before you come here buddy."
        
    except Exception as err:
        return str(err)

def add_user_line():
    pickupline_templates = user_templates
    print("Choose a template number (1-20):")
    try:
        template_number = int(input("> ")) - 1  
        if not (0 <= template_number < len(user_templates)):
            print("Template number out of range. Please choose between 1 and 20.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    template_to_show = pickupline_templates[template_number]
    placeholders_count = template_to_show.count("{}")  
    placeholder_representation = ['______'] * placeholders_count 
    print("Fill in the blanks for the following template:")
    print(template_to_show.format(*placeholder_representation))

    print(f"Enter {placeholders_count} word(s) separated by a comma to fill into the template:")
    words = input("> ").split(',')
    words = [word.strip() for word in words] 

    try:
        user_line = pickupline_templates[template_number].format(*words)
    except IndexError:
        print("Not enough words provided for the placeholders.")
        return
    except Exception as e:
        print(f"An unexpected formatting error occurred: {e}")
        return
    
    if is_line_valid(user_line): 
        print("Here's your custom pick-up line:")
        print(user_line)
        pickuplines['user_lines'].append(user_line)
        print("Nice! Your line was added!")
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
