"""
given a string, s, return the "reversed" string where all characters that are
not a letter stay in the same place, and all letters reverse their positions.

exmaple:
    input: "ab-cd"
    output: "dc-ba"

    input: "a-bC-dEF-ghIj"
    output: "j-Ih-gfE-dCba"

"""


def reverse_only_chars(s):
    # strings are immutable so we need to create an easy way to swap elements (an array)
    char_array = []
    # store the indices of the characters of the input string
    index_array = []
    # iterate through the string and populate the two arrays with their values.
    for i, char in enumerate(s):
        if char.isalpha():
            index_array.append(i)
        char_array.append(char)

    # intialize two pointers for the index_array
    i = 0
    j = len(index_array) - 1
    # iterate through the index array from front and back with two pointers.
    # swap the values that the pointers point to in the char_array
    while i < j:
        low_index = index_array[i]
        high_index = index_array[j]
        char_array[low_index], char_array[high_index] = char_array[high_index], char_array[low_index]
        i+=1
        j-=1

    # return a string of the reversed character word.
    # the non-alpha characters will remain in the same place.
    return "".join(char_array)

s = "ab-cd" # "dc-ba"
s = "a-bC-dEF-ghIj" # "j-Ih-gfE-dCba"
print(reverse_only_chars(s))
