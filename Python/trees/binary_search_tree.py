from binary_tree import Node, BinaryTree

class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)
        def walk(node, value):

            if node is None:
                self.root = new_node
                return

            if value < node.value:
                if not node.left:
                    node.left = new_node
                else:
                   walk(node.left)

            else:
                if not node.right:
                    node.right = new_node
                else:
                    walk(node.right)

        walk(self.root, value)

    def contains(self, value):
        def walk(node):
            if not node:
                return False
            if node.value == value:
                return True
            else:
                if value < node.value:
                    return walk(node.left)
                else:
                    return walk(node.right)

        found = walk(self.root)
        return found
