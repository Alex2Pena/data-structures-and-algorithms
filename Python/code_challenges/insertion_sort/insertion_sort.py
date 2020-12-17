# Sorts the array by using a tem variable
def sort_insertion_temp(arr):

    #for each index in the arrar...
    for i in range(len(arr)):

        j = i - 1 # j is equal the value before [i]
        temp = arr[i] # temp is equal to the value at [i]

        #While there is a [j] & temp value is less
        while j >= 0 and temp < arr[j]:

            arr[j + 1] = arr[j] # Advance the position of [j] by 1
            j = j - 1 # Re-assign [j]
        arr[j + 1] = temp # assigns [j] as the new temp

    # returns the sorted array
    return arr


# Sorts the array by swaping i & j
def sort_insertion_swap(arr):

    #for each index in the arrar...
    for i in range(len(arr)):

        j = i - 1 # set [j] to start where [i] is with each pass

        # While there is a [j] & is less than the next [j] index value
        while j >= 0 and arr[j + 1] < arr[j]:

            # Swaps the values once a new minimum is found
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j = j - 1

    # Returns sorted array
    return arr

# Alternate ending to do insertion sort with swap
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


