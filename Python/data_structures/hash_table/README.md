# Hashtables

In hashing, large keys are converted into small keys by using hash functions. The values are then stored in a data structure called hash table. The idea of hashing is to distribute entries (key/value pairs) uniformly across an array. Each element is assigned a key (converted key).

## Challenge

> Implement a Hashtable with the following methods:

> add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

> get: takes in the key and returns the value from the table.

> contains: takes in the key and returns a boolean, indicating if the key exists in the table already.

> hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
Required is a Node Class, Linked List Class, and Hastable Class
Included are ADD, CONTAINS, and GET methods for the Hash Table

## API
class Hashtable():

    # adds a new item to the Hashtable
        # gets a random "index/bucket" number
        # If there is already something at that index value then make a linked list at that index
        # append the new node with its key and value

    # Check to see if the table contains a specific key
        # assigns the hashed version of the original key
        # if it is found...
            # returns everything at the index/bucket
            # loops through the bucket/linkedlist...
                # If its in the "bucket" return True
        # else return False

    # returns the value found at a specific key
        # if we are given a key that exists in the hash table...
            # assigns the hashed "index/bucket" number
            # creates a list of all the nodes found in the "index/bucket"
            # Loops through the bucket and...
                # returns the value at [1] if the correct value is found
        # else return an error

    # Creates a random hash number
        # converts the key to a string
        # offset by 1
        # loop through all characters and...
        # takes the ascii value multiply by 599 then modulo by the size of the table
        # return the new randomly "hashed" number
