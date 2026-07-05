import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Sample data
data = [64, 25, 12, 22, 11]

# Bubble Sort Time
arr1 = data.copy()
start = time.time()
bubble_sort(arr1)
end = time.time()
bubble_time = end - start

# Selection Sort Time
arr2 = data.copy()
start = time.time()
selection_sort(arr2)
end = time.time()
selection_time = end - start

# Output
print("Original List :", data)
print("Bubble Sort   :", arr1)
print("Selection Sort:", arr2)

print("\nExecution Time")
print("Bubble Sort   :", bubble_time, "seconds")
print("Selection Sort:", selection_time, "seconds")