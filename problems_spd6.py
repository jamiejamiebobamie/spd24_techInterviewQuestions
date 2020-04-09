"""Monday, March 2nd"""

"""Write a function to check whether a given string is "smashable", meaning that
it’s a word in a predefined dictionary and can be reduced to a single character,
one character at a time, and every intermediate word during the reduction is
also in the dictionary of words. (Assume you have a file or list of valid
dictionary words, like /usr/share/dict/words)
Example: Given the word SPRINT as input, it should return the following:
SPRINT → PRINT → PINT → PIT → IT → I"""

def test_smashable(word):
    def reduce(word_part, i, result_array):
        if len(word_part) > 1 and i < len(word):
            test_array = list(word_part)
            j = 0
            while j < len(test_array):
                word_with_one_omission = ""
                for k, char in enumerate(test_array):
                    if j != k:
                        word_with_one_omission += char
                if word_with_one_omission in words:
                    result_array.append(word_with_one_omission)
                    return reduce(word_with_one_omission,i+1, result_array)
                j += 1
        else:
            return result_array

    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    words = set(words)
    f.close()

    result = [word]
    if reduce(word, 0, result):
        return result

print(test_smashable('split'))

"""Given a string and a predefined dictionary of words, find the 5 closest words
to the given string, where one character being substituted for another
counts as one step away.
Example: "clever" → ["clover", "claver", "carver", "glover", "sliver"]"""


def five_closest(word):
    def find_closest(num_of_letters_to_change):
        for _ in range (num_of_letters_to_change):
            while num_of_letters_to_change <= len(word) and result < 5:
                i, j = 0, 0
                while i < len(word):
                    while j < len(ALPHA_LOOKUP):
                        test_array = list(word)
                        test_array[i] = ALPHA_LOOKUP[j]
                        test_word = "".join(test_array)
                        if test_word in words:
                            result.append(test_word)
                        else:
                            j+=1
                    i+=1
        find_closest(num_of_letters_to_change+1)


    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    words = set(words)
    f.close()

    ALPHA_LOOKUP = list("abcdefghijklmnopqrstuvwxyz")

    result = []
    find_closest(1)
        return result

print(five_closest('split'))
