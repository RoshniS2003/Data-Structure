# Program to create a Singly Linked List in Python

# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store data
        self.next = None      # next node address


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None      # first node

    # Insert node at the end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Move to last node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        if self.head is None:
            print("Linked List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
sll = SinglyLinkedList()

# Insert elements
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(40)

# Display list
print("Singly Linked List:")
sll.display()