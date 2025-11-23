def movie_print(movies):
    for tittle in movies:
        if "The" in tittle:
            print(tittle.upper())


movie = ["The Godfather", "The Dark Knight", "The Godfather Part II",
         "12 Angry Men", "The Lord of the Rings", "Schindler's List", "Pulp Fiction"]
# for i in movie:
#     print(i.upper())
print("*********************************************")
movie_print(movie)
