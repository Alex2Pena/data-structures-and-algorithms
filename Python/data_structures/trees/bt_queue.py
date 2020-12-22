class Node(object):

    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

    def __str__(self):
        """
        """
        return f'<Node Value: { self.value }>'

    def __repr__(self):
        """
        """
        return f'<Node Value: { self.value }'

# needs to be imported by test
class InvalidOperationError(Exception):
    pass

class Queue():

    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def is_empty(self):
        if not self.left:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if not self.left:
            self.left = new_node
            self.right = new_node
            self.size += 1
            return new_node
        if value is None:
            raise InvalidOperationError('Node value cannot be none')
        self.right.next = new_node
        self.right = new_node
        self.size += 1
        if self.size == 1:
            self.left = new_node
        return new_node

    def dequeue(self):
        if self.left == None:
            raise InvalidOperationError('Cannot dequeue from empty queue')
        current_node = self.left
        if self.left:
            self.left = self.left.next
            self.size -= 1
        return current_node.value

    def peek(self):
        if self.left == None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.left.value
