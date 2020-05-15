"""input: [2,1,3]
output: True

input: [5,1,4,null,null,3,6]
output: false


assumptions:
    1. the children of a node, i, are at indices 2i+1 and 2i+2 of the input
        array.
    2. the input array does not contain parent nodes with a null value and
        children nodes with a real value.

"""
# no bsts were harmed in the making of this solution.
def is_valid(array_of_node_values):
    # iterate through the input array
    for i, node_value in enumerate(array_of_node_values):
        # intialize our children node indices given the current index in the array
        left_node_index, right_node_index = 2*i+1, 2*i+2
        # perform bounds checking on the array to ensure the index exists
        if left_node_index < len(array_of_node_values):
            # check to make sure the node's value isn't null.
            if array_of_node_values[left_node_index] != "null":
                # check the left child to see if it is greater than the parents node's value
                # if it is return False and print the offending nodes' values.
                if node_value < array_of_node_values[left_node_index]:
                    print(node_value, array_of_node_values[left_node_index])
                    return False
        # perform bounds checking on the array to ensure the index exists
        if right_node_index < len(array_of_node_values):
            # check to make sure the node's value isn't null.
            if array_of_node_values[right_node_index] != "null":
                # check the right child to see if it is less than the parent node's value
                # if it is return False and print the offending nodes' values.
                if node_value > array_of_node_values[right_node_index]:
                    print(node_value, array_of_node_values[right_node_index])
                    return False
    return True


array = [2,1,3]
array = [5,1,4,"null","null",3,6]
print(is_valid(array))
