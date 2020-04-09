# Give an array a of n numbers and a count k find the k largest values in the array a.

# a = [5,1,3,6,8,2,4,7], k=3 => [6,8,7]


def find_k_largest(a,k):
    # return the array if k is larger than the length of the array
    # initialize an empty array called 'result'
    # intialize a variable called 'minimum' and set its value to the first item in a
    # iterate through the input array:
        # if we have less than the desired return values:
            # add the current item to the result array
        # else if we have more than k items in the result array:
            # if item is greater than minimum:
                # iterate through the result array
                    # find the current minimum in the result array
                        # swap the current minimum with the new item in array that is larger than the minimum
        # reset the minimum to the new lowest in the result array
    # return the result


def find_k_largest(a,k):
    if k > len(a):
        return a
    # initialize an empty array called 'result'
    result = []

    # intialize a variable called 'minimum'
    # and set its value to the first item in a
    minimum = a[0]

    # iterate through the input array:
    for item in a:
        # if we have less than the desired return values
        if len(result) < k:
            # add the current item to the return values
            result.append(item)
        else:
            # if item is greater than minimum
            if item > minimum:
                # iterate through the result array
                for i, result_item in enumerate(result):
                    # find the current minimum in the result array
                    if result_item == minimum:
                        # swap the current minimum with the new item in array that is larger than the minimum
                        result[i] = item
        # reset the minimum to the new lowest in the result array
        minimum = min(result)
    # return the result
    return result

a = [5,8,1,3,6,2,4,7]#, k=3 => [6,8,7]
print(find_k_largest(a,3))
