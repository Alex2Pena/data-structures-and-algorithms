from linked_list.linked_list import Node, LinkedList

# Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

def zipList(l1, l2):

    list1 = l1.head
    list2 = l2.head
    merged_list = LinkedList()

    if list1 == None:
        return list2
    if list2 == None:
        return list1

    while list1 is not None and list2 is not None:

        if list1 is not None and merged_list.head == None:
                merged_list.insert(list1.data)
        else:
            merged_list.append_node(list1.data)

        if list2 is not None and merged_list.head == None:
                merged_list.insert(list2.data)
        else:
            merged_list.append_node(list2.data)

        if list1 and list1.next:
            list1 = list1.next
        else:
            list1 = None

        if list2 and list2.next:
            list2 = list2.next
        else:
            list2 = None

    return merged_list.head
