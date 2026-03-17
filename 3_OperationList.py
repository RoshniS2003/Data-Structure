# Program to demonstrate basic list operations

# Creating a list
numbers = [10, 20, 30, 40]
print("Original List:", numbers)

# 1. Append (Add element at the end)
numbers.append(50)
print("After Append:", numbers)

# 2. Insert (Add element at specific position)
numbers.insert(2, 25)
print("After Insert:", numbers)

# 3. Remove (Delete element)
numbers.remove(20)
print("After Remove:", numbers)

# 4. Access element
print("Element at index 3:", numbers[3])

# 5. Update element
numbers[1] = 100
print("After Update:", numbers)

# 6. Length of list
print("Length of List:", len(numbers))

# 7. Traversing the list
print("Traversing the list:")
for i in numbers:
    print(i)