class Node(object):
    """Class of node objects for Queue."""

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

# needs to be inported by test
class InvalidOperationError(Exception):
    pass

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        while self.top is None:
            return True
        if self.top:
            return False
        # return not self.top

    def push(self, value):
        if self.top == None:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        return self.top

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise InvalidOperationError("Method not allowed on empty collection")


    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
