from linked_list.linked_list import LinkedList
import pytest

@pytest.fixture
def data():
    ll1 = LinkedList()
    ll2 = LinkedList()
    return {'ll1' : ll1, 'll2' : ll2}

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
    ll.insert(10)
    actual = ll.insert(2)
    expected = 2
    assert actual == expected

# # The head property will properly point to the first node in the linked list
# def test_point_to_head():
#     ll = LinkedList()
#     ll.add_node_to_front(2)
#     ll.add_node_to_front(5)
#     ll.add_node_to_front(7)
#     actual = print_LL()
#     expected = 7
#     assert actual == expected

# # Can properly insert multiple nodes into the linked list
# def test_insert_multiple():
#     ll = LinkedList()
#     ll.add_node_to_front(2)
#     ll.add_node_to_front(5)
#     ll.add_node_to_front(7)
#     actual = ll.print_LL()
#     expected = [2,5,7]
#     assert actual == expected




# Will return true when finding a value within the linked list that exists

# Will return false when searching for a value in the linked list that does not exist

# Can properly return a collection of all the values that exist in the linked list


