
def sort_insertion_temp(arr):
    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr

def sort_insertion_swap(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j = j - 1
    return arr

