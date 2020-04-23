import random

def fisher_yates(data_array):

    index_array = []
    for i in range(len(data_array)):
        index_array.append(i) # 0 to len(data_array)-1

    for i, data in enumerate(data_array):
        # get a random index into the data_array
        index = random.choice(index_array)

        # swap the current element with the random index
        data_array[i], data_array[index] = data_array[index], data_array[i]

        # remove the index from the random choices
        # forgot how to ensure the correct index is used...
        index_array[-1], index_array[index] = index_array[index], index_array[-1]
        index_array.pop()

data_array = [1,2,3,4,5]
fisher_yates(data_array)
print(data_array)
