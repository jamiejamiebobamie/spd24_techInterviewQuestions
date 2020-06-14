"""
Form any string we can form a subsequence of that sting by deleting some number of characters (possibly no deletions).
Given two strings source and target, rturn the minimum number of subsequences of course such that their concatentation equals target.
If the task is impossible, rturn -1.

input source "abc" target = "abcbc"
output 2

input source "abc" target = "acdbc"
output -1

input source "xyz" target = "xyzxz"
output 3

("xz"+"y"+"xz")
"""
def shortest_way(source,target):
    # add individual characters
    substrings_in_source = set(source)
    # add entire word
    substrings_in_source.add(source)
    i = len(source) -1
    while (i > 0):
        # add substrings of word
        substrings_in_source.add(source[:i])
        substrings_in_source.add(source[abs(i):])
        i-=1

    unique_substrings_from_source_in_target = set()
    # we want the shortest way possible to form the target so we should look for
        # the largest substrings from source that make up the target
    i = len(target) -1
    while (i > 0):
        if target[:i] in substrings_in_source:
            unique_substrings_from_source_in_target.add(target[:i])
            # check if the current items in unique_substrings_from_source_in_target
                # set contains all of the letters necessary to form the target word
                # and return the count

        if target[abs(i):] in substrings_in_source:
            unique_substrings_from_source_in_target.add(target[abs(i):])
            # check if the current items in unique_substrings_from_source_in_target
                # set contains all of the letters necessary to form the target word
                # and return th count

        i-=1

    return -1

source =  "xyz"
target = "xyzxz"
shortest_way(source,target)
