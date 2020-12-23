# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{{ {str(self.data)} }} -> "

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

# Prints a strigified version of the LinkedList
    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += f"{{ {str(current.data)} }} -> "
            current = current.next
        return res + "NULL"

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
        current_node = self.head
        if current_node == None:
            return "Sorry no nodes present"
        if current_node.data == data:
            current_node.next = Node(newData, current_node.next)
            return
        found_node = None
        while current_node.next:
            if current_node.next.data == data:
                found_node = True
                current_node.next = Node(newData, current_node.next)
                return
            else:
                current_node = current_node.next
        if found_node != True:
            return "Could not find node"


# .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

    def insert_after(self, data, newData):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            if current_node.data == data:
                current_node.next = Node(newData, current_node.next)
                return
            current_node = current_node.next

# Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges. Example: [1,2,3,4,5,6,7] kth = 2
#                                                 ^

    def find_kth_value_from_end(self, kth):
        count = 0
        leader = self.head
        follower = self.head

        if kth < 0:
            raise ValueError("You cannot enter a negative integer")
        while count <= kth and leader:
            leader = leader.next
            count += 1
        while leader:
            leader = leader.next
            follower = follower.next
            count +=1
        if kth > count:
            raise IndexError("The list is not that big")
        return follower.data


# only run this when running directly as a "script"
if __name__ == "__main__":
    pass

