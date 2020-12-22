class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self):
        tree_arr = []

        def walk(node):
            if not node: return
            tree_arr.append(node.value)
            if node.left: walk(node.left)
            if node.right: walk(node.right)
        walk(self.root)
        return tree_arr


    def match_tree_preorder(self, arr):
        match_arr = []

        def match_walk(node, arr):
            if not node: return
            if node.value in arr: match_arr.append(node.value)
            if node.left: match_walk(node.left, arr)
            if node.right: match_walk(node.right, arr)
        match_walk(self.root, arr)
        return match_arr

def tree_intersection (tree_A, tree_B):
    # make a list of values in preorder
    tree_arr = tree_A.pre_order_traversal()
    match_arr = tree_B.match_tree_preorder(tree_arr)
    if len(match_arr) < 1: match_arr.append('No matches found :-(')
    return match_arr



if __name__ == "__main__":
    pass
