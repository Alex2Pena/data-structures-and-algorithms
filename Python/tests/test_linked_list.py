from data_structures.linked_list.linked_list import LinkedList
import pytest


# Test if class is imported
def test_import():
    assert LinkedList

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected

# Can properly insert into the linked list
def test_insert_front():
    ll = LinkedList()
    ll.insert(2)
    actual = ll.head.data
    expected = 2
    assert actual == expected

# # The head property will properly point to the first node in the linked list
def test_point_to_head():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.head.data
    expected = 5
    assert actual == expected

# # Can properly insert multiple nodes into the linked list
def test_insert_multiple():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(5)
    ll.insert(7)
    actual = [ll.head.data, ll.head.next.data, ll.head.next.next.data]
    expected = [7,5,2]
    assert actual == expected

# Will return true when finding a value within the linked list that exists
def test_includes_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    actual = ll.includes(2)
    expected = True
    assert actual == expected

# Will return false when searching for a value in the linked list that does not exist
def test_includes_false():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(4)
    expected = False
    assert actual == expected

# Can properly return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    actual = ll.return_all()
    expected = [4,3,2,1]
    assert actual == expected

# Can successfully add a node to the end of the linked list
def test_append():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.append_node(4)
    actual = ll.return_all()
    expected = [1,2,3,4]
    assert actual == expected

# Can successfully add multiple nodes to the end of a linked list



# Can successfully insert a node before a node located in the middle of a linked list
# @pytest.mark.skip("testing infinite loop")
def test_insert_before():
    ll = LinkedList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    ll.append_node(4)
    ll.append_node(5)
    ll.insert_before(3,2.5)
    actual = ll.return_all()
    expected = [1,2,2.5,3,4,5]
    assert actual == expected

# Can successfully insert a node before the first node of a linked list


# Can successfully insert after a node in the middle of the linked list
def test_insert_after():
    ll = LinkedList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    ll.append_node(4)
    ll.append_node(5)
    ll.insert_after(3,3.5)
    actual = ll.return_all()
    expected = [1,2,3,3.5,4,5]
    assert actual == expected

# Can successfully insert a node after the last node of the linked list


# Where k is greater than the length of the linked list
def test_is_k_longer_than_length():
    ll = LinkedList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    with pytest.raises(IndexError):
        ll.find_kth_value_from_end(4)

# Where k and the length of the list are the same
def test_is_k_same_as_length():
    ll = LinkedList()
    ll.append_node("a")
    ll.append_node("b")
    ll.append_node("c")
    actual = ll.find_kth_value_from_end(2)
    expected = "a"
    assert actual == expected

# Where k is not a positive integer
def test_negative_input():
    ll = LinkedList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    # test will pass if code in block causes expected ERROR
    with pytest.raises(ValueError):
        ll.find_kth_value_from_end(-1)

# Where the linked list is of a size 1
def test_single_node_ll():
    ll = LinkedList()
    ll.insert("a")
    actual = ll.find_kth_value_from_end(0)
    expected = "a"
    assert actual == expected

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_k_in_middle():
    ll = LinkedList()
    ll.append_node("a")
    ll.append_node(3)
    ll.append_node("3")
    actual = ll.find_kth_value_from_end(1)
    expected = 3
    assert actual == expected

