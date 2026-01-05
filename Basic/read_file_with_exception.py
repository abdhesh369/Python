filename = input("Enter the filename(xyz.txt): ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File contents:\n", content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Operation complete.")