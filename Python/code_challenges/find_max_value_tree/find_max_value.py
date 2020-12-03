from trees.binary_tree import Node, BinaryTree

def find_maximum_value(self):
    def walk(root, max_so_far):

        if not max_so_far or root.value > max_so_far:
            max_so_far = root.value
        if root.left:
            max_so_far = walk(root.left, max_so_far)
        if root.right:
            max_so_far = walk(root.right, max_so_far)
        return max_so_far

    return walk(self.root, self.root.value)

