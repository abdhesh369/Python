movies = ["Inception", "Tenet", "Interstellar", "Avengers", "Jack reacher"]

with open("movies.txt", "w") as file:
    for m in movies:
        file.write(m+"\n")

with open("movies.txt", "r") as file:
    lines = file.readlines()
    for n in lines:
        print(n)
