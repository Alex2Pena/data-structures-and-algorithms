import random
from .bt_queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)
        queue = Queue()
        if self.root != None:
            queue.enqueue(self.root)
            while not queue.is_empty():
                current_node = queue.dequeue()
                if not current_node.left:
                    current_node.left = new_node
                    return
                if current_node.right == None:
                    current_node.right = new_node
                    return
                if current_node.left:
                    queue.enqueue(current_node.left)
                if current_node.right:
                    queue.enqueue(current_node.right)
        else:
            self.root = new_node
        return

    def randomly_add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def walk(root):
            if not root.left:
                root.left = Node(value)
                return
            if not root.right:
                root.right = Node(value)
                return
            if random.randint(0, 1):
                walk(root.left)
            else:
                walk(root.right)

        walk(self.root)
            # randomly select a left or right node to walk through

    def find_maximum_value(self):
        max = None
        def walk(root):
            nonlocal max
            if not max or root.value > max:
                max = root.value
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return max

    def pre_order(self):
        values = []
        def walk(current):
            if not current:
                return

            values.append(current.value)
            walk(current.left)
            walk(current.right)

        walk(self.root)
        return values

    def in_order(self):
        values = []
        def walk(current):
            if not current:
                return

            walk(current.left)
            values.append(current.value)
            walk(current.right)

        walk(self.root)
        return values

    def post_order(self):
        values = []
        def walk(current):
            if not current:
                return

            walk(current.left)
            walk(current.right)
            values.append(current.value)

        walk(self.root)
        return values


    def breadth_first(self): # goes from top to bottom and left to right for each tree row
        values = [] # will store all node values in breadth first order
        queue = Queue() # instantiate a new empty queue
        queue.enqueue(self.root) # start at top of the tree (root)

        while not queue.is_empty(): # while the queue is not empty...
            current_root = queue.dequeue() # lets dequeue the node
            if not current_root:
                break
            values.append(current_root.value) # now append the value to the values list
            if current_root.left != None: # if there is a left child...
                queue.enqueue(current_root.left) # then lets enqueue it
            if current_root.right != None: # if there is a right child...
                queue.enqueue(current_root.right) # then lets enqueue it
        return values # return the entire values list
