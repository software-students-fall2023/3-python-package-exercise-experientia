import pyrizz

"""Main function for PyRizz."""

#ASCII art

print(" __    " + "    ____  _            ")
print("|__)   " + "   / __ \(_)_______    ")
print("|   \/ " + "  / /_/ / /_  /_  /    ")
print("    /  " + " / _, _/ / / /_/ /_    ")
print("       " + "/_/ |_/_/ /___/___/    ")

print("\n\n")

def main():
    print("Welcome to PyRizz! Your journey to getting a date begins here...\n")

    while True:
        
        print("What would you like to do today?\n")
        print("1. Get a random pick-up line hand-picked by the devs with a guaranteed 100% success rate.")
        print("2. Get a category-specific random pick-up line hand-picked by the devs with a guaranteed 100% success rate.")
        print("3. Have AI generate a pick-up line in your chosen category / language with a 50% success rate.")
        print("4. Have AI rate your pick-up line out of 10. Test it on AI before trying it on a human! ;)")
        print("5. Insert your own pick-up line to our database.\n")
        print("!! Type Q to quit !!\n")

        print("Enter your choice: ")
        user_input = input("> ")

        if user_input == "3":
            print("Enter a category / language: ")
            category = input("> ")
            print("\n" + pyrizz.get_ai_line(category), end = "\n\n")

        elif user_input == "q" or user_input == "Q":
            break

        print("Would you like to do something else? (y/n)")
        user_cont = input("> ")

        if user_cont == "n":
            break

        if user_cont == "y":
            continue
        
if __name__ == "__main__":
    main()