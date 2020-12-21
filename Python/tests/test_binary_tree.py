from trees.binary_tree import BinaryTree
from trees.binary_search_tree import BinarySearchTree


def test_import():
    assert BinaryTree
    assert BinarySearchTree

def test_instantiate_empty_tree():
    bt = BinaryTree()
    assert bt.root is None

def test_multiple_nodes():
    bt = BinaryTree()
    bt.add(1)
    bt.add(2)
    bt.add(3)
    assert bt.root.right.value == 3

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
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.pre_order()
    expected = [3,2,6]
    assert actual == expected

def test_return_inorder_traversal():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.in_order()
    expected = [2,3,6]
    assert actual == expected

def test_return_postorder_traversal():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(2)
    bst.add(6)
    actual = bst.post_order()
    expected = [2,6,3]
    assert actual == expected

def test_max():
    tree = BinaryTree()
    tree.randomly_add(3)
    tree.randomly_add(4)
    tree.randomly_add(11)
    tree.randomly_add(5)
    tree.randomly_add(9)
    assert tree.find_maximum_value() == 11

def test_breadth_first_empty():
    tree = BinaryTree()
    actual = tree.breadth_first()
    expected = []
    assert actual == expected

def test_breadth_first_single():
    tree = BinaryTree()
    tree.add(2)
    actual = tree.breadth_first()
    expected = [2]
    assert actual == expected

def test_breadth_first_many():
    tree = BinaryTree()
    tree.add(2)
    tree.add(11)
    tree.add(6)
    tree.add(9)
    tree.add(4)
    tree.add(9)
    tree.add(2)
    tree.add(99)
    tree.add(12)
    tree.add(7)
    actual = tree.breadth_first()
    expected = [2,11,6,9,4,9,2,99,12,7]
    assert actual == expected



