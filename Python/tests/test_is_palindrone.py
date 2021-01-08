import pytest
from code_challenges.is_palindrone.is_palindrone import Node, LinkedList

def test_import():
    assert LinkedList.isPalindrome

def test_empty_input():
   with pytest.raises(TypeError):
        LinkedList.isPalindrome()

def test_happy_path():
    llist = LinkedList()
    llist.head = Node('a')
    llist.head.next = Node('bc')
    llist.head.next.next = Node("d")
    llist.head.next.next.next = Node("dcb")
    llist.head.next.next.next.next = Node("a")
    actual = LinkedList.isPalindrome(llist)
    expected = True
    assert actual == expected

def test_False():
    llist = LinkedList()
    llist.head = Node('a')
    llist.head.next = Node('c')
    llist.head.next.next = Node("d")
    llist.head.next.next.next = Node("dcb")
    llist.head.next.next.next.next = Node("a")
    actual = LinkedList.isPalindrome(llist)
    expected = False
    assert actual == expected

