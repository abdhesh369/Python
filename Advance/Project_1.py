# Simple Calculator
xyz = True
while xyz:
    abc = True
    while abc:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")

        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            abc=False
            print(f"Result: {num1} + {num2} = {num1 + num2}") 
        elif choice == '2':
            abc=False
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            abc=False
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            abc=False
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid input\n")
            print("Enter a valid choice:")

    do = True
    while do:
        mood = input("\nWant to continue (Yes/No): ").lower()
        if mood == "yes":
            print("Okay, continuing...")
            do = False
        elif mood == "no":
            print("Exiting program...")
            xyz = False
            do = False
        else:
            print("Invalid input, please type Yes or No.")
