from .stack import Stack, Node

class InvalidOperationError(Exception):
    pass

class PseudoQueue:
    def __init__(self, in_stack = Stack(), out_stack = Stack()):
        self.in_stack = in_stack
        self.out_stack = out_stack
        self.count = 0

    def enqueue(self,value):
            self.count +=1
            self.in_stack.push(value)

    def dequeue(self):
        if self.out_stack.is_empty:
            while self.count>0:
                self.out_stack.push(self.in_stack.pop())
                self.count-=1
        return self.out_stack.pop()

    def __str__(self):
        output = ''
        cur =self.in_stack.top
        while cur:
            output+= f' -> {{ {cur.value} }}'
            cur = cur.next
        return output

# class PseudoQueue(Stack):
#     def __init__(self):
#         self.top = None
#         self.main = Stack()
#         self.temp = Stack()

#     def enqueue(self, value):
#         while not self.main.top:
#             self.temp.push(self.main.top.value)
#             self.main.pop()
#         self.main.push(value)
#         while self.temp.top:
#             self.main.push(self.temp.top.value)
#             self.temp.pop()
#         self.top = self.main.top

#     def dequeue(self):
#         if self.top:
#             output = self.top.value
#             self.main.pop()
#             self.top = self.main.top
#             return output

if __name__ == "__main__":
    pass

