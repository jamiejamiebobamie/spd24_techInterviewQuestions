"""
The problem was to write a function that will
print out the nodes of a binary tree in spiral order,
meaning it will print out odd levels from left to right
like a normal level order traversal but will print
out even levels from right to left,
the order visited is like in the attached screenshot

Spiral order: https://makeschoolstudents.slack.com/files/UM1ESSU94/F017H0SDGSE/screen_shot_2020-07-20_at_11.36.24_am.png

In your solution think about the different ways this can be implemented as
well as any tradeoffs between different approaches in terms of time and space
complexity.
"""

from collections import deque

def spiral_order(root):
    def level_order_traversal(level, arr):
        if len(queue):
            node = queue.pop_left()
            arr.append(node.data)
            # normal level order traversal
            queue.push(node.left)
            queue.push(node.right)
            level_order_traversal(level+1)
        return
    level = 1
    queue = deque() # nodes
    queue.push(root)
    normal_level_order = []
    reverse_level_order = []
    level_order_traversal(level,normal_level_order)
    level_order_traversal(level,reverse_level_order)
    print(normal_level_order)
    print(reverse_level_order)


# lookup:
    # queue methods
    # level order traversal
    # time compelxity of recursive functions vs iterative.


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
                # duplicates are allowed. (so not a binary search tree...)
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

root = BN(1)
tree = BTree(root)
# class binary_node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
# class binary_tree:
#     def __init__(self, root):
#         self.root = root
# # level 1
# root = binary_node(1)
# bt = binary_tree(root)
# # level 2
# two = binary_node(2)
# three =binary_node(3)
# four =binary_node(4)
# five =binary_node(5)
# six =binary_node(6)
# seven =binary_node(7)
# eight =binary_node(8)
# nine =binary_node(9)
# ten =binary_node(10)
# eleven =binary_node(11)
# twelve =binary_node(12)
# thirteen =binary_node(13)
# fourteen =binary_node(14)
# seven.left = fourteen
