rows= int(input("enter the number of rows\n "))
columns=int(input("enter the number of columns\n"))

matrix=[]
for i in range(rows):
    row = []
    for j in range(columns):
        element = input(f"Enter element for position ({i+1},{j+1}): ")
        row.append(element)
    matrix.append(row)


for rows in matrix:
    print(matrix)