import random
MAX_SCORE = 100

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
    limits, max_attempts = choose_difficulty()

    number = random.randint(1, limits)
    attempts = 0
    score = MAX_SCORE
    print(f"\nI have chosen a number between 1 and {limits}")

    while attempts < max_attempts:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Enter number only.")
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
            return True, attempts, score


while True:
    won, attempts, score = number_guess()

    print(f"Attempts used: {attempts}")
    print(f"Score: {score}")

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Exiting game.")
        break
