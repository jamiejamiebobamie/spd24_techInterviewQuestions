#
# Array Problems – used Jan 22 (baseline) and April 2 (brainstorming)
# Problem 1
# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]
#
# Problem 2
# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
#
# Problem 3
# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
"""
problem 1

iterate through the smaller list
store the {t - m(i) : m(i)} in a dict
iterate through the larger list and see if any of the entries are in the dict
if not return none or -1

simplification: smaller array would be better

problem 2

use a min_heap (max_heap?) to keep the max values in sorted descending order
popping from the back of the list to remove the smallest when the heap as grown to size k
return heap

simple: already sorted.
simplification: make k the size of the array to start as it gets rid of it
simplification: a data structure that keeps k elements in sorted order based on value max/min

problem 3

simplification: guarantee there is a solution, positive numbers.

iterate through the smaller list
store the {t - m(i) - + range : m(i)} in a dict

the range is some range above and below t - m(i)

iterate through the larger array and see if any of the entries are in the dict
find the closest one to the target by lookng at the squared difference of (m(i) + (t - m(i)))**2
(t - m(i)) being the corresponding entry in the larger array

"""

# problem one from above.
a = [1,2,3,4,1,8,5,3,6]
t = 9


def findPairs(a,t):

    lookup = {}
    result = []

    for val in a:
        key = t-val
        if val not in lookup:
            lookup[key] = val

    for val in a:
        key = t-val

        valid = lookup.get(val, False)

        if valid:
            result.append([val, valid])

    return result

print(findPairs(a,t))
