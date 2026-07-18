import random

def number_guessing_game():
    secret_number = random.randint(1, 100)

    attempts = 0

    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I have kept a number between 1 and 100. Let's see in how many moves you can find it?")

    while True:

        guess = int(input("What is your guess? = "))

        attempts = attempts + 1

        if guess < secret_number:
            print("You should enter a LARGER number")
        elif guess > secret_number:
            print("You should enter a SMALLER number")
        else:
            print("\n*** Congratulations, you guessed it right! ***")
            print(f"The hidden number = {secret_number}")
            print(f"Your total number of attempts = {attempts}")
            break

number_guessing_game()