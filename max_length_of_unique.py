"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of
arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26"""

arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]

def max_length_of_concat(arr):
    result = []
    def recur(index, concat):
        char_set = set(concat)
        if len(concat) != len(char_set):
            return
        else:
            result.append(concat)
            for i in range(len(arr)):
                recur(i, concat+arr[i])

    recur(-1, "")

    return max([len(word) for word in result])

print(max_length_of_concat(arr))
