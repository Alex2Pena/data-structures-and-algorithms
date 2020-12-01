import random
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

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

            # randomly select a left or right node to walk through
            if random.randint(0, 1):
                walk(root.left)
            else:
                walk(root.right)

        walk(self.root)




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
