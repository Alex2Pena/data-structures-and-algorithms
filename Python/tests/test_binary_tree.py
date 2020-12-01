from trees.binary_tree import BinaryTree
from trees.binary_search_tree import BinarySearchTree


def test_import():
    assert BinaryTree
    assert BinarySearchTree

def test_instantiate_empty_tree():
    bt = BinaryTree()
    assert bt.root is None

# def test_multiple_nodes():
#     bt = BinaryTree()
#     bt.add(1)
#     bt.add(2)
#     bt.add(3)
#     bt.add(4)

def test_instantiate_single_root():
    bst = BinarySearchTree()
    bst.add(1)
    assert bst.root.value == 1


def test_add_to_left():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    assert bst.root.left.value == 2

def test_add_to_right():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    assert bst.root.right.value == 6

def test_return_preorder_traversal():
    bst = BinarySearchTree()
    bt = BinaryTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.pre_order()
    expected = [3,2,6]
    assert actual == expected

def test_return_inorder_traversal():
    bst = BinarySearchTree()
    bt = BinaryTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.in_order()
    expected = [2,3,6]
    assert actual == expected

def test_return_postorder_traversal():
    bst = BinarySearchTree()
    bt = BinaryTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.post_order()
    expected = [2,6,3]
    assert actual == expected
