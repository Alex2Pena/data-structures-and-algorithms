from data_structures.linked_list.linked_list import LinkedList

class Hashtable():
    def __init__(self, size):
        self.size = size
        self.indicies = [None] * self.size

    # adds a new item to the Hashtable
    def add(self, key, val):
        # gets a random "index/bucket" number
        hashed = self._hash(key)
        # If there is already something at that index value then make a linked list at that index
        if not self.indicies[hashed]: self.indicies[hashed] = LinkedList()
        # append the new node with its key and value
        self.indicies[hashed].append_node([key, val])

    # Check to see if the table contains a specific key
    def contains(self, key):
        # assigns the hashed version of the original key
        hashed_key = self._hash(key)
        # if it is found...
        if self.indicies[hashed_key]:
            # returns everything at the index/bucket
            key_list = self.indicies[hashed_key].return_all()
            # loops through the bucket/linkedlist...
            for vals in key_list:
                # If its in the "bucket" return True
                if vals[0] == key: return True
        # else return False
        return False

    # returns the value found at a specific key
    def get(self, key):
        # if we are given a key that exists in the hash table...
        if self.contains(key):
            # assigns the hashed "index/bucket" number
            hashed_key = self._hash(key)
            # creates a list of all the nodes found in the "index/bucket"
            key_list = self.indicies[hashed_key].return_all()
            # Loops through the bucket and...
            for values in key_list:
                # returns the value at [1] if the correct value is found
                if values[0] == key: return(values[1])
        # else return an error
        raise ValueError('Key does not exist.')

    # Creates a random number
    def _hash(self, key):
        # converts the key to a string
        if not isinstance(key, str): key = str(key)
        # offset by 1
        ascii_val = 1
        # loop through all characters and...
        for char in key: ascii_val += ord(char)
        # takes the ascii value multiply by 599 then modulo by the size of the table
        hashed_key = ascii_val * 599 % self.size
        # return the new randomly "hashed" number
        return hashed_key

    def __str__(self):
        output = ''
        for index in self.indicies:
            if index: output += ('').join(str(elem) for elem in index.return_all())
        if not output: return 'None'
        return output
