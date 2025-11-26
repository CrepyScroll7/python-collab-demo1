import random

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"
COLOR_BLACK = "\033[31"

def greet():
    """Ask for user's name and greet them."""
    name = input("What's your name? ")
    print(f"{COLOR_CYAN}Hello, {name}! Welcome to the GitHub collaboration demo.{COLOR_RESET}")

def guess_the_number():
    """Simple number guessing game with 3 attempts."""
    print(f"{COLOR_YELLOW}I'm thinking of a number from 1 to 10. You have 3 tries.{COLOR_RESET}")
    secret_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            attempt = int(input("Enter a number: "))
        except ValueError:
            print(f"{COLOR_RED}Please enter a valid number.{COLOR_RESET}")
            continue

        if attempt == secret_number:
            print(f"{COLOR_GREEN}Correct! You guessed the number.{COLOR_RESET}")
            return
        elif attempt < secret_number:
            print("The secret number is higher.")
        else:
            print("The secret number is lower.")

        attempts -= 1
        print(f"You have {attempts} attempts left.\n")

    print(f"{COLOR_RED}Out of attempts! The number was {secret_number}.{COLOR_RESET}")

def show_menu():
    """Display main menu."""
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Greet")
        print("2. Guess the number")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            greet()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(f"{COLOR_RED}Invalid option. Try again.{COLOR_RESET}")

if __name__ == "__main__":
    show_menu()