lines = [
    "Start log\n",
    "Second entry\n",
]

with open("log.txt", "w") as f:
    f.writelines(lines)

with open("log.txt", "a+") as f2:
    f2.write("Third entry\n")
    f2.seek(0)
    print(f2.read())
