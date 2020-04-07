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

# problem three from above.

def find_closest(a,b,t):
    LOOKUP = {}

    if len(a) < len(b):
        shorter_array = a
        longer_array = b
    else:
        shorter_array = b
        longer_array = a

    end_of_range = 2
    start_of_range = end_of_range * -1

    for val in shorter_array:
        index_of_range = start_of_range
        while index_of_range < end_of_range:
            # widen the net in the hopes that
                # one of the keys is in the other array.
            key = t - val + index_of_range
            LOOKUP[key] = val
            index_of_range += 1

    minimum_abs_diff = float('inf')
    lowest = None
    for val in longer_array:
        if val in LOOKUP:
            lookup_sum = val + LOOKUP[val]
            diff = t - lookup_sum
            # need to compare the magnitude of a difference
                # that is both positive and negative so
                # multiply it by itself to remove the sign.
            temp_abs_diff, test_abs_diff = minimum_abs_diff, diff * diff
            minimum_abs_diff = min(test_abs_diff, minimum_abs_diff)
            if temp_abs_diff != minimum_abs_diff:
                lowest = [val, LOOKUP[val]]
    return lowest


a=[9, 13, 1, 8, 12, 4, 0, 5]
b=[3, 17, 4, 14, 6]
t=21

print(find_closest(a,b,t)) #[4, 17]
