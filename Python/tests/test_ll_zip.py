from data_structures.linked_list.linked_list import LinkedList
from code_challenges.ll_zip.ll_zip import zipList

# import pytest

# @pytest.fixture
# def sample_lists():
#     l1 = LinkedList()
#     l2 = LinkedList()
#     l1.append_node("a")
#     l1.append_node("b")
#     l1.append_node("c")
#     l2.append_node(1)
#     l2.append_node(2)
#     l2.append_node(3)
#     return [l1, l2]


def test_import():
    assert zipList

def test_same_size_lists():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append_node("a")
    l1.append_node("b")
    l1.append_node("c")
    l2.append_node(1)
    l2.append_node(2)
    l2.append_node(3)
    actual = zipList(l1,l2)
    expected = ["a", 1, "b", 2, "c", 3]

    while actual:
        assert actual.data == expected.pop(0)
        actual = actual.next

def test_list1_smaller():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append_node("a")
    l1.append_node("b")
    l2.append_node(1)
    l2.append_node(2)
    l2.append_node(3)
    actual = zipList(l1,l2)
    expected = ["a", 1, "b", 2, 3]

    while actual:
        assert actual.data == expected.pop(0)
        actual = actual.next

def test_list2_smaller():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append_node("a")
    l1.append_node("b")
    l1.append_node("c")
    l2.append_node(1)
    l2.append_node(2)
    actual = zipList(l1,l2)
    expected = ["a", 1, "b", 2, "c"]

    while actual:
        assert actual.data == expected.pop(0)
        actual = actual.next

def test_list1_empty():
    l1 = LinkedList()
    l2 = LinkedList()
    l2.append_node(1)
    l2.append_node(2)
    l2.append_node(3)
    actual = zipList(l1,l2)
    expected = [1, 2, 3]

    while actual:
        assert actual.data == expected.pop(0)
        actual = actual.next

def test_list2_empty():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append_node("a")
    l1.append_node("b")
    l1.append_node("c")
    actual = zipList(l1,l2)
    expected = ["a", "b", "c"]

    while actual:
        assert actual.data == expected.pop(0)
        actual = actual.next

def test_missing_both():
    l1 = LinkedList()
    l2 = LinkedList()
    actual = zipList(l1, l2)
    expected = None
    assert actual == expected


