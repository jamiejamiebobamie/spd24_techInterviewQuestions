"""
https://leetcode.com/problems/verifying-an-alien-dictionary/description/

953. Verifying an Alien Dictionary
Easy

684

274

Add to List

Share
In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order. The order of the alphabet is some
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is
sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is
shorter (in size.) According to lexicographical rules "apple" > "app",
because 'l' > '∅', where '∅' is defined as the blank character which is
less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters."""


def verify(words, order):
    # create a lookup dictionary that converts the characters in the language to
        # integers depending on their order in the language (starts at 0)
    LOOKUP = {char : i for i, char in enumerate(order)}
    # intialize an empty array to store the words transformed into num arrays
        # should be low to high if the words are verified as True
    low_to_high_num_arrays = []
    # iterate through the words in the 'words' parameter array
        # for each character turn it into a number
        # the most significant nums are at the front, but every letter matters
        # during the comparison.
    for word in words:
        word_num = []
        for char in word:
            num = LOOKUP[char]
            word_num.append(num)
        # append the num_arrays to the low_to_high_num_arrays for comparison
        low_to_high_num_arrays.append(word_reversed_num)
    # iterate through the low_to_high_num_arrays if one of the later items has
        # a lower value than the former return False, otherwise True
    for i, word_nums in enumerate(low_to_high_num_arrays):
        if i != 0:
            if low_to_high_num_arrays[i-1] > low_to_high_num_arrays[i]:
                return False
    return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(verify(words, order)) # true
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(verify(words, order)) # false
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(verify(words, order)) # false
