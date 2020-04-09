"""Wednesday, March 4th
Main Activity: Remote Coding
Everyone is going to solve two technical interview problems remotely with a new partner.
This is great practice for technical phone screens and take-home interview challenges.
Choose a new partner, then choose two problems from the lists below to solve together.

Challenging problems we’ve seen before:
Given an array of k singly-linked lists, each of whose values are in
sorted order, combine all nodes (do not create new nodes) into one
singly-linked list with all values in order.
Given a binary search tree, convert it into a sorted doubly-linked list
by modifying the original tree nodes (do not create new nodes).
Let’s say a binary tree is "superbalanced" if the difference between the
depths of any two leaf nodes is at most one. Write a function to check if
a binary tree is "superbalanced".

LeetCode problems we haven’t seen before:
Jump Game
Median of two sorted arrays
Best time to buy and sell stock

Choose your own new problem at LeetCode.com, HackerRank.com, FireCode.io,
or anywhere..."""


"""Given an array of k singly-linked lists, each of whose values are in
sorted order, combine all nodes (do not create new nodes) into one
singly-linked list with all values in order."""

class LL_node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LL():
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def add(self, data):
        new_node = LL_node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head, self.tail = new_node, new_node

    def print_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        print(result)

    # doesn't work.
    # need to add remaining elements of longer list to the end
    # need to error check for edge cases
        # (like duplicate values in both lists or one list)
    def combine(self, LL2):
        node1, node2 = self.head, LL2.head
        while node1 and node2:
            if node1.data <= node2.data:
                temp = node1.next
                node1.next = node2
                node1 = temp
            elif node1.data >= node2.data:
                temp = node2.next
                node2.next = node1
                node2 = temp
        # add remaining nodes to end
        # if node1:
        #     temp.next = node2
        # elif node2:
        #     node2.next = node1

# [1, 3, 5, 7]
# [2, 4, 6, 8]


# myLL1 = LL()
# myLL1.add(1)
# myLL1.add(3)
# myLL1.add(5)
# myLL1.add(5)
# myLL1.add(7)
# myLL1.add(33)
#
# myLL1.print_list()
#
# myLL2 = LL()
# myLL2.add(2)
# myLL2.add(4)
# myLL2.add(4)
# myLL2.add(5)
# myLL2.add(6)
# myLL2.add(8)
# myLL2.add(15)
#
# myLL2.print_list()
#
# myLL1.combine(myLL2)
# myLL1.print_list()

"""
 https://leetcode.com/problems/jump-game-ii/

 Given an array of non-negative integers,
 you are initially positioned at the first index of the array.

 Each element in the array represents your maximum jump length at that position.

 Your goal is to reach the last index in the minimum number of jumps.

 Example:

 Input: [2,3,1,1,4]
 Output: 2
 Explanation: The minimum number of jumps to reach the last index is 2.
     Jump 1 step from index 0 to 1, then 3 steps to the last index.
 Note:

 You can assume that you can always reach the last index.
 """

jump_array = [2,3,1,1,4] # 2
# doesn't work.
def find_min_jumps(jump_array):
    def count_jumps(count, i):
        if i == len(jump_array) - 1:
             result.append(count)

        elif i < len(jump_array):
            num_of_jumps = jump_array[i]
            count_jumps(count+1, jump_array[num_of_jumps+1])

    result = []
    count_jumps(0, 0)
    return min(result)

# print(find_min_jumps(jump_array))

"""
http://romanenco.com/jumps-problem
public class MinJumpsLinear {

    public int jump(int[] A) {
        if (A.length < 2) {
            return 0;
        }
        int steps = 0;
        int distance = 0;
        int update = 0;
        for (int i = 0; i < A.length - 1; i++) {
            if (i + A[i] > distance) {
                distance = i + A[i];
            }
            if (i == update) {
                steps++;
                update = distance;
                if (distance >= A.length - 1) {
                break;
            }
            }
        }
        return steps ;
    }

}"""

jump_array = [1,1,3,1,1] # 2

def test_jumps(array):
    if len(array) < 2:
        return 0

    count = 0
    distance = 0
    update = 0

    for index in range(len(array)):
        # the current place in the array plus the number of jumps at that place
        # is greater than the currently stored distance, set the distance to that jump
        if index + array[index] > distance:
            distance = index + array[index]
        # if index is equal to the update
        if index == update:
            # incrmeent the count
            count += 1
            # set update to the distance
            update = distance
            # check to ensure we have't over jumped
            if distance > len(array) - 1:
                # if we have... we have our answer??
                break

    return count - 1

# print(test_jumps(jump_array))


"""There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time
complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5"""

nums1 = [1, 2]
nums2 = [3, 4]

nums1 = [1, 3]
nums2 = [2]

def find_median(list1, list2):
    minimum = min(list1[0], list2[0]) # 1 or 3 => 1
    maximum = max(list1[len(list1)-1], list2[len(list2)-1]) # 2 or 4  4

    return float(minimum+maximum)/2

# print(find_median(nums1,nums2))


"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an
algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def max_profit(array):
    def compute_diff(buy, sell):
        return sell - buy
    # the buy must be before the sell (have a lower index)
    minimum_buy = 0
    min_buy_index = -1

    # the sell must be after the buy (have a higher index)
    maximum_sell = 0
    max_sell_index = len(array)

    # maximum profit = maximum_sell - minimum_buy
    for i, stock_price in enumerate(array):
        # adjust buy
        if compute_diff(minimum_buy,maximum_sell) < compute_diff(stock_price, maximum_sell) and i < max_sell_index:
            minimum_buy = stock_price
            min_buy_index = i
        # adjust sell
        if compute_diff(minimum_buy,maximum_sell) < compute_diff(minimum_buy, stock_price) and i > min_buy_index:
            maximum_sell = stock_price
            max_sell_index = i

    return compute_diff(minimum_buy,maximum_sell)

print(max_profit([7,1,5,3,6,4]))
