class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        # Creates a Node with (data) and give it a next property
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        # Initialize an empty list
        self.head = None

    # A utility function to check if str is palindrome
    # or not
    def isPalindromeUtil(self, string):
        # If string is equal to the reversed version of its self...
        if (string == string[::-1]):
             return True
        else:
            return False

    # Returns true if string formed by linked list is
    # palindrome
    def isPalindrome(self):
        if not self.head:
            return TypeError
            
        node = self.head

        # Append all nodes to form a string
        temp = []
        while (node is not None):
            temp.append(node.data)
            node = node.next
        string = "".join(temp)
        return self.isPalindromeUtil(string)

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.head = Node('a')
llist.head.next = Node('bc')
llist.head.next.next = Node("d")
llist.head.next.next.next = Node("dcb")
llist.head.next.next.next.next = Node("a")
llist.printList()
# llist = {a} -> {bc}  -> {d} -> {dcb} -> {a}
# temp = ["a", "bc", "d", "dcd", "a"]
# string = "abcddcda"


# Call the function
# print(llist.isPalindrome())

