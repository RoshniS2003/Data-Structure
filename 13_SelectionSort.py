# Selection Sort Program

# Input list
arr = [64, 25, 12, 22, 11]

# Selection Sort
for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the elements
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Print the sorted list
print("Sorted List:", arr)