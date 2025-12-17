# Simple Calculator
import math
def add(x, y): return x+y
def subtract(x, y): return x-y
def product(x, y): return x*y
def divide(x, y): return "Error: Division by zero is not allowed" if y == 0 else x/y
def power(x, y): return x**y
def modulus(x,y): return "Error: Division by zero is not allowed" if y == 0 else x % y
def square_root(x): return "Error: Negative Number" if x < 0 else math.sqrt(x)


def calculation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power(x^y)")
    print("6. Modulus(x%y)")
    print("7. Square Root(x**y)")

    choice = input("Enter choice (1-7): ")
    try:
        if choice == '7':
            num1 = float(input("\nEnter number: "))
            print(f"Result: √{num1} = {square_root(num1)}")
        else:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {product(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} ** {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        else:
            print("Invalid input\n")
    except:
        print("Enter valid input")


xyz = True
while xyz:
    calculation()
    while True:
        mood = input("\nWant to continue (Yes/No): ").lower()
        if mood == "yes":
            print("Okay, continuing...")
            break
        elif mood == "no":
            print("Exiting program...")
            xyz = False
            break
        else:
            print("Invalid input, please type Yes or No.")
