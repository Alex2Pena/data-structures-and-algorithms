import pytest

from stacks_and_queues.pseudo_queue import Stack, PseudoQueue, InvalidOperationError
test_stack = Stack()
test_stack.push(11)
test_stack.push(12)
test_stack.push(20)


def test_enqueue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.top.value
    expected = "apple"
    assert actual == expected

def test_dequeue():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected

def test_peek():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected

def test_peek_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError):
        q.peek()

def test_enqueue_one():
    q = PseudoQueue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected

def test_enqueue_two():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected

def test_dequeue_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()

def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected

def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected

def test_is_empty():
    q = PseudoQueue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_exhausted():
    q = PseudoQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
