import os
import random
import pathlib
import json
from pyrizz.pickuplines import pickuplines
from pyrizz.templates import templates


PROJECT_ROOT = f"{pathlib.Path(__file__).parent.resolve()}/../.."

def get_lines(category='all'): 
    if category not in pickuplines:
        return ("Category does not exist!")

    else: 
        return pickuplines[category]

def get_random_line(): 
    allpickuplines = get_lines('all')
    return random.choice(allpickuplines)

def get_random_category_line(category='all'):
    category_pickupline = get_lines(category)
    return random.choice(category_pickupline)

def get_ai_line(category, client) -> str:
    try:
        if (category != "" and len(category) <= 50):
            response = client.ChatCompletion.create(
                model = "gpt-3.5-turbo",
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

def rate_line(pickup_line, client) -> str:
    try:
        if (pickup_line != ""):
            response = client.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages =
                    [{"role": "user", "content": f"Rate this pickup line out of 10 (whole numbers only): {pickup_line} In your response, STRICTLY follow the format of (nothing else): rating/10 - snazzy comment."},]
            )
            message = response.choices[0]['message']
            ai_rating_response = "{}".format(message['content'])
            return ai_rating_response
        
        else:
            return "No pickup line? You gotta use our other features before you come here buddy."
        
    except Exception as err:
        return str(err)

def create_line():
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
            print("\nLooks great! Try it on a human now and meet your match!")
            return(user_line)
            
        except Exception as e:
            print(f"An error occurred while inserting the line into the database: {e}")
    else: 
        return("Your pick-up line doesn't pass our checks.")

def is_line_valid(user_line):
    if len(user_line) > 140:
        return False
    
    return True
