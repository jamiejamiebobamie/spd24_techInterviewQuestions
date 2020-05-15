"""given a time in teh format of "HH:MM", form the next closest time by resuing the digits.

input 19:34 output 19:39
it's not 19:33 because time only goes forwards
"""
# not working
def find_closest_time(stringTime):

    def recur():
        for perm in permutation(nums):
            sum = 0
            powers = [1, 10, 100, 1000]
            for num in perm:
                sum+= num * powers.pop()
            print(sum)
            # messed-up. nums can repeat...
            # also time is based on a 0 to 60 scale so
            # decimal comparison wouldn't have worked (?)

    nums = []
    for stringNum in stringTime:
        if stringNum != ":":
            nums.append(int(stringNum))

    recur()

# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Python function to print permutations of a given list
def permutation(arr):
    # If arr is empty then there are no permutations
    if len(arr) == 0:
        return []
    # If there is only one element in arr then, only
    # one permuatation is possible
    if len(arr) == 1:
        return [arr]

    # Find the permutations for arr if there are more than 1 characters
    l = [] # empty list that will store current permutation
    # Iterate the input array and calculate the permutation
    for i in range(len(arr)):
       m = arr[i]
       # Extract arr[i] or m from the list. rem_arr is remaining list
       rem_arr = arr[:i] + arr[i+1:]
       # Generating all permutations where m is first element
       for p in permutation(rem_arr):
           l.append([m] + p)
    return l

# Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print(p)

stringTime = "19:34"
find_closest_time(stringTime)
