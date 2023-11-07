import pyrizz as pyrizz

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
        
        if user_input == "3":
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
            print("Invalid Response.")
            user_cont = input("Would you like to try again? (y/n): ")

            while user_cont not in ["n", "y"]:
                print("\nPlease provide a valid input (y/n)")
                user_cont = input("> ")

            if user_cont == "n":
                break

        
if __name__ == "__main__":
    main()