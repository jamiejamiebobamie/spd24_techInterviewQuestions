"""
Rearrange an array with alternate high and low elements

Given an array of integers, rearrange the array such that every second
element of the array is greater than its left and right elements.
Assume no duplicate elements are present in the array.


 {9, 6, 8, 3, 7} => {6, 9, 3, 8, 7}
 {6, 9, 2, 5, 1, 4} => {6, 9, 2, 5, 1, 4}
 """

# function takes in array
# sort array # [3,6,7,8,9]
# check to see if array is odd or even
# if odd:
    # break array into:
        # len(a)//2+1 = smaller [3,6,7]
        # len(a)//2 = larger [8,9]
# result = []
# j,k = 0,0
# iterate through smaller array
 # if i % 2 == odd:
  # result.append(larger_array[k])
  # k+=1
# else:
  # result.append(smaller_array[j])
  # j+=1

# resut = [3,8,]

def interleave(array):
    sorted_array = sorted(array)
    if len(sorted_array) % 2: # odd
        end_index = len(sorted_array)//2+1
    else:
        end_index = len(sorted_array)//2
    first_half = sorted_array[:end_index]
    second_half = sorted_array[end_index:]

    result = []
    j,k = 0,0
    for i, item in enumerate(sorted_array):
        if j+k < len(sorted_array):
            if i % 2: # odd
                result.append(second_half[k])
                k+=1
            else:
                result.append(first_half[j])
                j+=1
    return result

array = [6, 9, 2, 5, 1, 4]
array = [9, 6, 8, 3, 7]
array = [1, 2, 3, 4, 5, 6, 7]
# print(interleave(array)) # [3, 8, 6, 9, 7]

# in-place
# O(n)
def interleave1(a):
    # [6, 9, 2, 5, 1, 4]
    #  {9, 6, 8, 3, 7} => {6, 9, 3, 8, 7}
    count = 0
    finished = False
    while not finished:
        finished = True
        for i, item in enumerate(a):
            if i < len(a)-1:
                if not i % 2: # even :: lesser value amounts
                    if a[i] > a[i+1]:
                        a[i], a[i+1] = a[i+1], a[i]
                        finished = False
                else: # odd :: greater value amounts
                    if a[i] < a[i+1]:
                        a[i], a[i+1] = a[i+1], a[i]
                        finished = False
            count+=1
    print(count)
    return a

print(interleave1(array))
