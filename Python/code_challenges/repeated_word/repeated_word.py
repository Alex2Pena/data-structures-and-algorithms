import string

def find_repeated_word(input_string):
    stripped_string = input_string.translate(str.maketrans('', '', string.punctuation))
    lower_string = stripped_string.lower()

    myset=set()
    for i in lower_string.split(" "):
        if(i in myset):
            return (i)
        else:
            myset.add(i)
    return None
