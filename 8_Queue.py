# Create empty queue
queue = []

# Enqueue operation
def enqueue():
    element = int(input("Enter element to enqueue: "))
    queue.append(element)
    print(element, "added to queue")

# Dequeue operation
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        removed = queue.pop(0)
        print(removed, "removed from queue")

# Display queue
def display():
    print("Queue elements are:", queue)

# Main program
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")
