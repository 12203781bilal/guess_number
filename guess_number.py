# guess_number.py
import random

def play_game():
    print("Welcome to Guess the Number!")
    lower = 1
    upper = 100
    secret = random.randint(lower, upper)
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}.")
    print("Type 'quit' to exit anytime.\n")

    while True:
        guess = input("Your guess: ").strip()
        if guess.lower() == "quit":
            print(f"Bye! The number was {secret}.")
            break

        if not guess.isdigit():
            print("Please enter a valid integer (or 'quit').")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            # Ask to play again
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                secret = random.randint(lower, upper)
                attempts = 0
                print(f"\nNew number between {lower} and {upper} — go!\n")
            else:
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    play_game()
