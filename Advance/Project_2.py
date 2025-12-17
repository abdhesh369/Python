import random

MAX_ATTEMPTS = 10

def number_guess():
    print("\nWelcome to the Game!")
    print("I have a number between 1 and 100.")
    print("Try to guess it.")

    number = random.randint(1, 100)
    attempts = 0
    score = 100

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Enter a valid integer.")
            continue

        attempts += 1

        if guess > number:
            score -= 5
            print("Too high! Try again.")
        elif guess < number:
            score -= 5
            print("Too low! Try again.")
        else:
            print("\nCongratulations! You guessed it.")
            print(f"Number: {number}")
            print(f"Attempts: {attempts}")
            print(f"Score: {score}")
            return attempts, score

    print("\nGame Over!")
    print(f"The number was: {number}")
    print(f"Score: {score}")
    return attempts, score


running = True
while running:
    attempts, score = number_guess()

    while True:
        choice = input("\nPlay again? (yes/no): ").lower()
        if choice == "yes":
            break
        elif choice == "no":
            print("Exiting game.")
            running = False
            break
        else:
            print("Invalid input. Type yes or no.")
