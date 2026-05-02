# Program to demonstrate Column-Major Order Representation
# Easy Python Program

# Creating a 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nColumn-Major Order Representation:")

# Accessing elements column by column
for j in range(cols):      # column loop
    for i in range(rows):  # row loop
        print(matrix[i][j], end=" ")