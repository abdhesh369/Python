import random
MAX_ATTEMPTS = 10


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice.")


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
