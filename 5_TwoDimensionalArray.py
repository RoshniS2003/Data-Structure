# Creating a 2D array using list of lists
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the 2D array
for row in array:
    for element in row:
        print(element, end=" ")
    print()