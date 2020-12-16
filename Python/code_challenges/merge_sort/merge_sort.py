def merge_sort(input_arr):

  # If the length of the input_arr is greater than 1...
  if len(input_arr) > 1:
    # Divide the array in half
    mid = len(input_arr) // 2
    #Assign both halves to variables
    left = input_arr[:mid]
    right = input_arr[mid:]
    # Call the merge_sort function recursively on both halves
    merge_sort(left)
    merge_sort(right)
    i = 0 # left half iterator
    j = 0 # right half iterator
    k = 0 # whole input_arr iterator

    # Whie there is still a left AND a right side
    while i < len(left) and j < len(right):
        # If the left sides value is less
        if left[i] <= right[j]:
            # Move the MAIN iterator to the left side
            input_arr[k] = left[i]
            # Increment left side
            i += 1
        # If the right sides value is less
        else:
            # Move the MAIN iterator to the right side
            input_arr[k]= right[j]
            # Increment right side
            j += 1
        # Finally increment the MAIN
        k += 1

    # Handels remaining side if uneven
    while i < len(left):
        input_arr[k] = left[i] # Move to the left
        k += 1
        i += 1
    while j < len(right):
        input_arr[k] = right[j] # Move to the right
        k += 1
        j += 1

    #Ultimatly return the original input_arr sorted
    return input_arr


if __name__ == "__main__":
  input_arr = [8, 4, 23, 42, 16, 15]
  merge_sort(input_arr)
  print(input_arr)
