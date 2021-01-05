import re

# Function to validate URL
# using regular expression
def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

# Removes any spaces and replaces them with %20
def sanitize_URL(string):
    if not string:
        raise TypeError
    new_string = string.replace(" ", "%20")
    # After replacing any spaces check validity of URL format
    if (isValidURL(new_string) == True):
        return new_string
    else:
        return "Invalid URL format"

# print(sanitize_URL("http://code.org/hour of code.html"))
