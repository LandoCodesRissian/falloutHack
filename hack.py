import random
import os

def load_words():
    return ["APPLE", "BERRY", "CHIEF", "DREAM", "FAITH", "GHOST", "HORSE", "JOKER", "LEMON", "MOOSE"]

def choose_password(words):
    return random.choice(words)

def compare_words(word, guess):
    return sum(a == b for a, b in zip(word, guess))

def print_terminal(words, password):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen to mimic terminal
    print("\033[92m")  # Set the text color to green
    print("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL")
    print("ENTER PASSWORD NOW\n")
    for word in words:
        print(word)

def main():
    words = load_words()
    password = choose_password(words)
    attempts = 4
    print_terminal(words, password)

    while attempts > 0:
        guess = input("\n\033[97mEnter your guess: \033[92m").upper()  # Input prompt
        if guess == password:
            print("\033[96mSuccess! You've hacked in!")
            break
        else:
            matches = compare_words(password, guess)
            print(f"{matches} letter(s) match!")
            attempts -= 1
            if attempts == 0:
                print("\033[91mFailure! System locked.")
                break
            else:
                print(f"\033[93m{attempts} attempts left.")

if __name__ == "__main__":
    main()
