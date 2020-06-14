
"""
given a sorted array of ints return the sorted squared array of that array

"""

# O(n) time complexity
# O(n) space complexity
# https://www.youtube.com/watch?v=4eWKHLSRHPY
def sorted_squared(arr):
    negative_and_zero = []
    positive = []
    for n in arr:
        if n <= 0:
            negative_and_zero.append(n**2)
        else:
            positive.append(n**2)
    i = 0
    j = len(negative_and_zero)-1
    k = 0

    # merge the two sorted arrays.
        # negative is sorted in descending order, so iterate from the back.
    while i < len(positive) and j >= 0:
        if positive[i] < negative_and_zero[j]:
            arr[k] = positive[i]
            i+=1
        else:
            arr[k] = negative_and_zero[j]
            j-=1
        k+=1

    # remove remaining elements from positive or negative arrays
        # it will only be one array or the other.
    while i < len(positive):
        arr[k] = positive[i]
        i+=1
        k+=1
    while j >= 0:
        arr[k] = negative_and_zero[j]
        j-=1
        k+=1

    return arr

arr = [-10,-5,-4,-2,-1,0,1,2,3,4,5,6]
print(sorted_squared(arr))
