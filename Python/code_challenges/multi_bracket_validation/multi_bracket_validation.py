def multi_bracket_validation(input):
    # Creates an empty stack
    stack = []

    # If no input exists return TypeError
    if not input:
        return TypeError
    # Loop for checking string
    for char in input:
        # If an opening char is found append it to the stack
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        # If a closing bracket is found
        elif char == '}' or char == ')' or char == ']':
            # If the stack is not empty
            if len(stack) == 0:
                return False
            # Remove and compare the last item in the stack
            top_element = stack.pop()
            # If it does not match acording to the comapre function
            if not compare(top_element, char):
                return False
    # Check if the stack is not empty
    if len(stack) != 0:
        return False
    # If it is empty...
    return True

# function to check if opening char matches closing char
def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False

