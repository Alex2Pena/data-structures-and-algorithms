from data_structures.linked_list.linked_list import LinkedList

class Hashtable():
    def __init__(self, size):
        self.size = size
        self.indicies = [None] * self.size

    def add(self, key, val):
        hashed = self._hash(key)
        if not self.indicies[hashed]: self.indicies[hashed] = LinkedList()
        self.indicies[hashed].append_node([key, val])

    def contains(self, key):
        hashed_key = self._hash(key)
        if self.indicies[hashed_key]:
            key_list = self.indicies[hashed_key].return_all()
            for vals in key_list:
                if vals[0] == key: return True
        return False

    def get(self, key):
        if self.contains(key):
            hashed_key = self._hash(key)
            key_list = self.indicies[hashed_key].return_all()
            print(key_list)
            for values in key_list:
                if values[0] == key: return(values[1])
        raise ValueError('Key does not exist.')

    def _hash(self, key):
        if not isinstance(key, str): key = str(key)
        ascii_val = 1
        for char in key: ascii_val += ord(char)
        hashed_key = ascii_val * 599 % self.size
        return hashed_key

    def __str__(self):
        output = ''
        for index in self.indicies:
            if index: output += ('').join(str(elem) for elem in index.return_all())
        if not output: return 'None'
        return output
