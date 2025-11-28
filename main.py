import random

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"
COLOR_MAGENTA = "\033[35m"  # <--- NUEVO

def greet():
    """Ask for user's name and greet them."""
    name = input("What's your name? ")
    print(f"{COLOR_CYAN}Hello, {name}! Welcome to the GitHub collaboration demo.{COLOR_RESET}")

# se tiene que cambiar para recibir estadisticas y pues el puntaje basicament
def guess_the_number(stats): # <--- MODIFICADO: AHORA RECIBE 'stats'
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
            
            # --- INICIO DEL CODIGO NUEVO (LOGICA DE PUNTOS) ---
            points_earned = attempts * 50  # Mas intentos sobran = mas puntos
            stats["wins"] += 1
            stats["score"] += points_earned
            print(f"{COLOR_MAGENTA}You earned {points_earned} points! Total score: {stats['score']}{COLOR_RESET}")
            # --- FIN DEL CODIGO NUEVO ---
            
            return
        elif attempt < secret_number:
            print("The secret number is higher.")
        else:
            print("The secret number is lower.")

        attempts -= 1
        print(f"You have {attempts} attempts left.\n")

    print(f"{COLOR_RED}Out of attempts! The number was {secret_number}.{COLOR_RESET}")
    
    # --- INICIO DEL CODIGO NUEVO (REGISTRO DE DERROTA) ---
    stats["losses"] += 1
    print(f"{COLOR_MAGENTA}Don't give up! Current score: {stats['score']}{COLOR_RESET}")
    # --- FIN DEL CODIGO NUEVO ---

# --- pa mantenerte actualiza de puntajes ---
def show_statistics(stats):
    """Show the current game session statistics."""
    print(f"\n{COLOR_MAGENTA}=== SESSION SCOREBOARD ==={COLOR_RESET}")
    print(f"Games Won:    {stats['wins']}")
    print(f"Games Lost:   {stats['losses']}")
    print(f"Total Score:  {stats['score']} points")
    print(f"==========================\n")
# -----------------------------------------------

def show_program_info():
    """Show information about the program."""
    print(f"{COLOR_GREEN}=== Program Information ==={COLOR_RESET}")
    print("Project: GitHub Collaboration Demo")
    print("Description: A basic project for practicing branches and pull requests.")
    print("Author: Your Name")

def show_menu():
    """Display main menu."""
    
    # --- INICIO DEL CODIGO NUEVO (INICIALIZAR DICCIONARIO) ---
    # Creamos un diccionario para guardar los datos mientras el programa corre
    game_stats = {
        "wins": 0,
        "losses": 0,
        "score": 0
    }
    # --- FIN DEL CODIGO NUEVO ---

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Greet")
        print("2. Guess the number")
        print("3. Show Statistics") 
        print("4. Program Info")     
        print("5. Exit")             

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            greet()
        elif choice == "2":
            # Pasamos la variable game_stats a la funcion
            guess_the_number(game_stats) # <--- MODIFICADO
        elif choice == "3":
            # Llamamos a la nueva funcion
            show_statistics(game_stats)  # <--- NUEVO
        elif choice == "4":
            show_program_info()
        elif choice == "5":
            print("Goodbye!")
            # Mostramos el puntaje final antes de salir
            show_statistics(game_stats)  # <--- NUEVO DETALLE FINAL
            break
        else:
            print(f"{COLOR_RED}Invalid option. Try again.{COLOR_RESET}")

if __name__ == "__main__":
    show_menu()