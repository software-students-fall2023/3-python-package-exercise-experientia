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
        print("1. Get a random pick-up line")
        print("2. Get a category-specific random pick-up line (romantic, clever, geeky, dev)")
        print("3. Have AI generate a pick-up line in your chosen category / language (no more than 50 characters)")
        print("4. Have AI rate your pick-up line out of 10. Test it on AI before trying it on a human! ;)")
        print("5. Create your very own pickup line!.\n")
        print("!! Type Q to quit !!\n")

        print("Enter your choice: ")
        user_input = input("> ")

        if user_input == "1":
            print("\n" + pyrizz.get_random_line(), end = "\n\n")

        elif user_input == "2":
            print("Select a category: ")
            print("1 - Romantic")
            print("2 - Clever")
            print("3 - Geeky")
            print("4 - Developer Lines")
            category_index = input("> ")
            category_index = int(category_index) 
            if category_index in range(1, 4):
                if(category_index == 1): 
                    category_val = "romantic"
                elif(category_index == 2): 
                    category_val = "clever"
                elif(category_index == 3):
                    category_val = "geeky"
                elif(category_index == 4):
                    category_val = "dev"
                print("\n" + pyrizz.get_random_category_line(category_val), end = "\n\n")
        
        elif user_input == "3":
            print("Enter a category / language: ")
            category = input("> ")
            print("\n" + pyrizz.get_ai_line(category), end = "\n\n")
        
        elif user_input == "4":
            print("Type your pickup line: ")
            pickup_line = input("> ")
            print("\n" + pyrizz.rate_line(pickup_line), end = "\n\n")

        elif user_input == "5": 
            pyrizz.create_line()

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