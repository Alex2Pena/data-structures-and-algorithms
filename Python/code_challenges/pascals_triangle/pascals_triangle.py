def pascals_triangle(n):
    if type(n) is not int:
        raise TypeError('You must input an int')
    # Creates an empty array and sets the value of the first index
    new_arr = [[1],]
    # loops through each index
    for index in range(n-1):
    # Center and printing happens here
	    new_arr.append(next_row(new_arr[index]))
# printing needs to happen here
    return new_arr

def next_row(arr):
    # creates an empty nested array
	new_arr = [arr[0]]
    #
	for index, num in enumerate(arr[:-1]):

		new_arr.append(num+arr[index+1])

	new_arr.append(arr[-1])

	return new_arr
print(pascals_triangle(10))

# -------------------------------------------------------------------------


# def PascalTriangle(n):

#     triangle_row = [1]
#     y = [0]
#     for x in range(n):
#         print(triangle_row)
#         triangle_row=[left+right for left,right in zip(triangle_row+y, y+triangle_row)]
#     return n>=1

# PascalTriangle(10)
