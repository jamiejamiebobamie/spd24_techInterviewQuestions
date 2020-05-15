"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""

#O(n**2)
def find_repeated(s):
    sequences_of_ten = {}

    if len(s) < 10:
        return []

    i = 0
    while i < len(s) - 10 - 1:
        test_sequence = s[ i : i + 10]
        if test_sequence not in sequences_of_ten:
            sequences_of_ten[test_sequence] = 1
        else:
            sequences_of_ten[test_sequence] += 1
        i+=1

    return [key for key in sequences_of_ten.keys() if sequences_of_ten[key] > 1]

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(find_repeated(s))
