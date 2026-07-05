# Insertion Sort Program

arr = [12, 11, 13, 5, 6]

# Traverse through the array
for i in range(1, len(arr)):
    key = arr[i]      # Current element
    j = i - 1

    # Move elements greater than key one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

# Print the sorted array
print("Sorted Array:")
print(arr)