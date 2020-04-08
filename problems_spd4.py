"""Wednesday, February 12th
Warmup
Grab a whiteboard and marker.
Draw a diagram of a binary search tree containing 6 strings inserted in
the following order: 'red', 'orange', 'yellow', 'green', 'blue', 'purple'.
Label the root node and its references that link to its children. Label all
leaf nodes.
Compare your diagram to 2 other students’ diagrams. Are your structures identical?
"""

class BN:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree:

    def __init__(self, root=None):
        self.root = root
        self.num_nodes = 0

    def add(self,data):
        new_node = BN(data)
        if self.num_nodes == 0:
            self.root = new_node
            self.num_nodes += 1
        else:
            curr = self.root
            last = None
            while curr:
                last = curr
                if curr.data < data:
                    curr = curr.right
                elif curr.data > data or curr.data == data:
                    curr = curr.left
            if last.data < data:
                last.right = new_node
            elif last.data > data or last.data == data:
                last.left = new_node

    def inorder_traversal(self):
        def recur(node):
            if node:
                recur(node.left)
                tree_data.append(node.data)
                recur(node.right)
            return tree_data

        # left,root,right
        tree_data = []
        node = self.root
        recur(node)
        return tree_data

    def find_nodes_that_sum(self, n):
        def recur(node):
            if node:
                # move as far down the tree as possible
                recur(node.right)
                recur(node.left)

                # then begin to add values
                if node.data in LOOKUP:
                    # return the two nodes and their data
                    node1_object = LOOKUP[node.data]
                    node1_data = node1_object.data
                    node1 = (node1_object,node1_data)

                    node2_object = node
                    node2_data = node.data
                    node2 = (node2_object,node2_data)

                    return (node1,node2)
                else:
                    desired_value = n - node.data
                    # should we care about overwriting values in the dict?
                    LOOKUP[desired_value] = node

        LOOKUP = {}
        node = self.root
        return recur(node)


# 'red', 'orange', 'yellow', 'green', 'blue', 'purple'

# myTree = BTree()
# myTree.add('red')
# print(myTree.inorder_traversal())
# myTree.add('orange')
# print(myTree.inorder_traversal())
# myTree.add('yellow')
# myTree.add('green')
# myTree.add('blue')
# myTree.add('purple')
# print(myTree.inorder_traversal())
# ['blue', 'green', 'orange', 'purple', 'red', 'yellow']

"""
# 'red', 'orange', 'yellow', 'green', 'blue', 'purple'

                    red
            orange          yellow
    green       purple
blue

"""


"""
Activity
Write your answers to these in your notebook:
Choose a problem below at the appropriate difficulty level for your own experience.
Draw a diagram of a normal or simple input case that you should attempt to solve first.
What are edge case inputs that could be more challenging to handle in your
solution? Write these down (or draw a small diagram) to identify them and not
worry about them.
Can you break the problem down into smaller pieces and solve each part separately?
Can you simplify any of the parts so you can make progress and then expand it later?

Binary Tree Problems
Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
Given a binary search tree containing integers and a target integer, come up
with an efficient way to locate two nodes in the tree whose sum is equal to the
target value.
Given a binary tree containing numbers, find the maximum sum path (the path that
has the largest sum of node values). The path may start and end at any node in the tree.
Let’s say a binary tree is "superbalanced" if the difference between the depths
of any two leaf nodes is at most one. Write a function to check if a binary tree
is "superbalanced".

Homework – Due next week: Wednesday, February 19th
Fully solve at least two of the above binary tree problems in real working code.
Use your idea sketches and pseudocode, type it in your code editor, run some
test cases, and debug your code so it works correctly. Implement at least
one solution for 2 or more of the problems above."""


"""
PROBLEM 1
Given a binary search tree containing integers and a target integer, come up
with an efficient way to locate two nodes in the tree whose sum is equal to the
target value.


idea:
given a tree and a number n
we can create a lookup dictionary of desired_values and nodes that contain the
compliment of that value that adds to 'n'. as we traverse the tree we build the
dictionary as well as look for the desired_values.

example:
            tree:
                                    1
                            0               2
                    -1                             3

            n = 0

assumptions:
    the tree has nodes with numbers
    n is a real, not complex integer number that may be positive or negative
    the tree may or may not contain two numbers that sum to n

simplification:
    just try to build the dictionary...
"""

# [1,0,2,3,-1]
myTree = BTree()
myTree.add(1)
myTree.add(0)
myTree.add(2)
myTree.add(3)
myTree.add(-1)
print(myTree.inorder_traversal())
print(myTree.find_nodes_that_sum(5))
# There's seems to be some issues... it doesn't work for all sums...


"""
PROBLEM 2
Let’s say a binary tree is "superbalanced" if the difference between the depths
of any two leaf nodes is at most one. Write a function to check if a binary tree
is "superbalanced".

idea:
we need to write a function that keeps track of the height/depth.
the issue / difficult part of it has to do with that each node has two paths...

we can create a wrapper function that has an empty array
when we traverse down the tree we increment a count.
when we reach a leaf node (node.left and node.right == none) we append the count
to the array that is in the wrapper function.

once every leaf has pushed its count to the array

we get the min and max counts from the array and if their difference is greater
than one then the tree is not superbalanced.


"""
