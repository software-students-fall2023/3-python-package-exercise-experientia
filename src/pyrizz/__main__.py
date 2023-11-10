# Uncomment when using pytest and uploading the package to PyPi
import pyrizz.pyrizz as pyrizz

# Uncomment when testing the __main__.py file locally
# import pyrizz as pyrizz

"""Main function for PyRizz."""

#ASCII art

print(" ________  ___    ___ ________  ___  ________  ________        ")
print("|\   __  \|\  \  /  /|\   __  \|\  \|\_____  \|\_____  \       ")
print("\ \  \|\  \ \  \/  / | \  \|\  \ \  \\\\|___/  /|\|___/  /|      ")
print(" \ \   ____\ \    / / \ \   _  _\ \  \   /  / /    /  / /      ")
print("  \ \  \___|\/   / /   \ \  \\\\  \\\\ \  \ /  /_/__  /  /_/__     ")
print("   \ \__\ __/   / /     \ \__\\\\ _\\\\ \__\\\\________\\\\________\   ")
print("    \|__||\____/ /       \|__|\|__|\|__|\|_______|\|_______|   ")
print("         \|____|/                                               ")

print("\n")

def main():
    openai_client = None
    print("Welcome to PyRizz! Your journey to getting a date begins here...")

    while True: 
        print("\nWhat would you like to do today?\n")
        print("1. Get a random pick-up line")
        print("2. Get a category-specific random pick-up line (romantic, clever, geeky, dev)")
        print("3. Create your line with one of our templates with randomly selected ASCII art.")
        print("4. List available templates for pick-up lines.\n")
        print("Use AI for your pickup lines: ")
        print("5. Enter your API key to use AI functionality.")
        print("6. Have AI generate a pick-up line in your chosen category / language (no more than 50 characters)")
        print("7. Have AI rate your pick-up line out of 10. Test it on AI before trying it on a human! ;) \n")
        
        print("!! Type Q to quit !!\n")

        print("Enter your choice: ")
        user_input = input("> ")

        if user_input == "1":
            print("\n" + pyrizz.get_random_line(), end = "\n")

        elif user_input == "2":
            print("Select a category: ")
            print("1 - Romantic")
            print("2 - Clever")
            print("3 - Geeky")
            print("4 - Developer Lines")
            category_index = input("> ")
            if (category_index.isdigit()): 
                category_index = int(category_index) 
                if(category_index in range(1, 5)):
                    if(category_index == 1): 
                        category_val = "romantic"
                    elif(category_index == 2): 
                        category_val = "clever"
                    elif(category_index == 3):
                        category_val = "geeky"
                    elif(category_index == 4):
                        category_val = "dev"
                    print("\n" + pyrizz.get_random_category_line(category_val), end = "\n")
                else: 
                    print("Please make sure it is a number from 1-4. \n")
            else: 
                print("Not a valid input! \n")

        elif user_input == "3": 
            template_number, words = pyrizz.get_user_input_for_line()
            line = pyrizz.create_line(template_number, words)
            if line:
                print("\nHere's your custom pick-up line:")
                print(line + "\n")

        elif user_input == "4":
            print("Here are the available templates:")
            templates = pyrizz.list_templates()
            for idx, template in enumerate(templates, 1):
                print(f"Template {idx}: {template}")

        elif user_input == "5":
            print("Please enter your API key.")
            user_api_key = input("> ")
            openai_client = pyrizz.init_openai(user_api_key)
        
        elif user_input == "6":
            if openai_client:
                print("Enter a category / language: ")
                category = input("> ")
                print("\n" + pyrizz.get_ai_line(category, openai_client), end = "\n\n")
            else:
                print("\nYou need to enter an API key first. Select 5!\n")
        
        elif user_input == "7":
            if openai_client:
                print("Type your pickup line: ")
                pickup_line = input("> ")
                print("\n" + pyrizz.rate_line(pickup_line, openai_client), end = "\n\n")
            else:
                print("\nYou need to enter an API key first. Select 5!\n")

        elif user_input == "q" or user_input == "Q":
            break
        
        else:
            print("\nInvalid Response.")
        
        while True:
            user_cont = input("Would you like to continue? (y/n): ")
            if user_cont in ["y", "n"]:
                break
            else:
                print("\nPlease provide a valid input (y/n)")

        if user_cont == "n" or user_cont == "q" or user_cont == "Q":
            break
        
if __name__ == "__main__":
    main()