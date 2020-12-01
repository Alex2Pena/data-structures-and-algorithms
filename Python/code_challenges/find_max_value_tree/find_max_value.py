from trees.binary_tree import Node, BinaryTree

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
