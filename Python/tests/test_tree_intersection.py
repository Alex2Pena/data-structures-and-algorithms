import pytest
from code_challenges.tree_intersection.tree_intersection import Node, BinaryTree, tree_intersection

def test_tree_intersection_matches(tree_a, tree_b):
    assert tree_intersection(tree_a, tree_b) == [150, 75, 125, 250, 350, 500]

def test_tree_intersection_no_match(tree_a, tree_c):
    assert tree_intersection(tree_a, tree_c) == ['No matches found :-(']

def test_tree_intersection_empty_array(tree_a):
    empty_tree = BinaryTree()
    assert tree_intersection(tree_a, empty_tree) == ['No matches found :-(']



@pytest.fixture
def tree_a():
    test_tree = BinaryTree()
    test_tree.root = Node(150)
    test_tree.root.left = Node(100)
    test_tree.root.left.left = Node(75)
    test_tree.root.left.right = Node(160)
    test_tree.root.left.right.left = Node(125)
    test_tree.root.left.right.right = Node(175)
    test_tree.root.right = Node(250)
    test_tree.root.right.left = Node(200)
    test_tree.root.right.right = Node(350)
    test_tree.root.right.right.left = Node(300)
    test_tree.root.right.right.right = Node(500)
    return test_tree

@pytest.fixture
def tree_b():
    test_tree = BinaryTree()
    test_tree.root = Node(150)
    test_tree.root.left = Node(101)
    test_tree.root.left.left = Node(75)
    test_tree.root.left.right = Node(161)
    test_tree.root.left.right.left = Node(125)
    test_tree.root.left.right.right = Node(176)
    test_tree.root.right = Node(250)
    test_tree.root.right.left = Node(201)
    test_tree.root.right.right = Node(350)
    test_tree.root.right.right.left = Node(301)
    test_tree.root.right.right.right = Node(500)
    return test_tree

@pytest.fixture
def tree_c():
    test_tree = BinaryTree()
    test_tree.root = Node(15)
    test_tree.root.left = Node(10)
    test_tree.root.left.left = Node(7)
    test_tree.root.left.right = Node(16)
    test_tree.root.left.right.left = Node(12)
    test_tree.root.left.right.right = Node(17)
    test_tree.root.right = Node(25)
    test_tree.root.right.left = Node(20)
    test_tree.root.right.right = Node(35)
    test_tree.root.right.right.left = Node(30)
    test_tree.root.right.right.right = Node(50)
    return test_tree
