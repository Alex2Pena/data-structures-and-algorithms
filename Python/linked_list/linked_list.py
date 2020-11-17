# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
    def insert(self, data):
        old_head = self.head
        self.head = Node(data, self.head)
        self.head.next = old_head

# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    def includes(self, data):
        if self.head == None:
            return False
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            if current_node.data == data:
                return True
        return False

# returns all values in Linked_list
    def return_all(self):
        all_values = []
        current_node = self.head
        while current_node != None:
            all_values.append(current_node.data)
            print(all_values)
            current_node = current_node.next
        return all_values

# .append(value) which adds a new node with the given value to the end of the list
    # def append(self, data)
    def append_node(self, data):
        newNode = Node(data, next=None)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

# .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node

    def insert_before(self, data, newData):
        newNode = Node(data, next=None)
        current_node = self.head
        if current_node == None:
            return "Sorry no nodes present"
        else:
            found_node = None
            while current_node:
                if current_node.next == data:
                    found_node = True
                    before_insert = current_node
                    after_insert = current_node.next
                    before_insert.next = newNode
                    newNode.next = after_insert
                    current_node = current_node.next
                else:
                    current_node = current_node.next
            if found_node != True:
                return "Could not find node"


# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

    # def insert_after(data, newData)

# only run this when running directly as a "script"
if __name__ == "__main__":
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.return_all()

