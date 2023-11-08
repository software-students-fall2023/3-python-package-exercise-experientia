import pyrizz.pyrizz as pyrizz

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
    print("Welcome to PyRizz! Your journey to getting a date begins here...\n")

    while True:    
        print("What would you like to do today?\n")
        print("1. Get a random pick-up line hand-picked by the devs with a guaranteed 100% success rate.")
        print("2. Get a category-specific random pick-up line hand-picked by the devs with a guaranteed 100% success rate.")
        print("3. Have AI generate a pick-up line in your chosen category / language (no more than 50 characters) with a 50% success rate.")
        print("4. Have AI rate your pick-up line out of 10. Test it on AI before trying it on a human! ;)")
        print("5. Insert your own pick-up line to our database.\n")
        print("!! Type Q to quit !!\n")

        print("Enter your choice: ")
        user_input = input("> ")

        if user_input == "1":
            print("\n" + pyrizz.get_random_line(), end = "\n\n")

        if user_input == "2":
            category_list = pyrizz.get_dev_line_categories()
            print("Select a category: ")
            for i, category in enumerate(category_list):
                print(f"{i + 1}. {category}")

            category_index = input("> ")
            category_index = int(category_index) if category_index.isdigit() else 4
            category_val = ''
            if category_index in range(1, 4):
                category_val = category_list[category_index - 1]
            print("\n" + pyrizz.get_random_categorized_line(category_val), end = "\n\n")
        
        if user_input == "1":
            # Some execution
            pass
        
        elif user_input == "2":
            # Some execution
            pass

        elif user_input == "3":
            print("Enter a category / language: ")
            category = input("> ")
            print("\n" + pyrizz.get_ai_line(category), end = "\n\n")
        
        elif user_input == "4":
            print("Type your pickup line: ")
            pickup_line = input("> ")
            print("\n" + pyrizz.rate_line(pickup_line), end = "\n\n")

        elif user_input == "5": 
            pyrizz.add_user_line()

        elif user_input == "q" or user_input == "Q":
            break
        
        else:
            print("\nInvalid Response.")
        
        while True:
            user_cont = input("Would you like to try again? (y/n): ")
            if user_cont in ["y", "n"]:
                break
            else:
                print("\nPlease provide a valid input (y/n)")

        if user_cont == "n" or user_cont == "q" or user_cont == "Q":
            break
        
if __name__ == "__main__":
    main()