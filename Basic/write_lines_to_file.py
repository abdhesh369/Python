lines = [
    "Python is powerful\n",
    "File handling is easy\n",
    "I am learning step by step\n"
]

with open("notes.txt", "w") as f:
    f.writelines(lines)
