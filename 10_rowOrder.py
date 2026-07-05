# Row-Major Order Representation

# Create a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Convert to row-major order (flatten row-wise)
row_major = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        row_major.append(matrix[i][j])

print("\nRow-Major Order Representation:")
print(row_major)