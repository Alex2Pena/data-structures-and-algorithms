# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
    def __str__(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(''.join("{} -> ".format(*k) for k in enumerate(elements))+'NULL')

# Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    def insert(self, node):
        node.next = self.head
        self.head = node
        return self.head


# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.



# only run this when running directly as a "script"
# if __name__ == "__main__":




# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
# Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
# Structure and Testing
# Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

# Write tests to prove the following functionality:

# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list
# Ensure your tests are passing before you submit your solution.

# Stretch Goal
# Create a new branch called doubly-linked-list, and, using the resources available to you online, implement a doubly linked list (completely separate from your singly linked list).
