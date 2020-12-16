class Node(object):

    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

    # def __str__(self):
    #     """
    #     """
    #     return f'<Node Value: { self.value }>'

    # def __repr__(self):
    #     """
    #     """
    #     return f'<Node Value: { self.value }'

# needs to be imported by test
class InvalidOperationError(Exception):
    pass

class Queue(object):

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
            self.size += 1
            return new_node
        if value is None:
            raise InvalidOperationError('Node value cannot be none')
        self.back.next = new_node
        self.back = new_node
        self.size += 1
        if self.size == 1:
            self.front = new_node
        return new_node

    def dequeue(self):
        if self.front == None:
            raise InvalidOperationError('Cannot dequeue from empty queue')
        current_node = self.front
        if self.front:
            self.front = self.front.next
            self.size -= 1
        return str(current_node.value)

    def peek(self):
        if self.front == None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return str(self.front.value)
