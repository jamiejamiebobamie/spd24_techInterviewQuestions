"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.

The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

"""

# O(n**2 runtime due to pop_biggest_stone method iterating through the list each time...)
def last_stone_weight(arr):
    while len(arr) != 1:
        biggest_stone = pop_biggest_stone(arr)
        second_biggest_stone = pop_biggest_stone(arr)
        if biggest_stone != second_biggest_stone:
            arr.append(biggest_stone-second_biggest_stone)
    return arr[0]

def pop_biggest_stone(arr):
    max_stone = float('-inf')
    max_stone_index = -1
    for i, item in enumerate(arr):
        if max_stone < item:
            max_stone_index = i
            max_stone = item
    arr[max_stone_index], arr[len(arr)-1] = arr[len(arr)-1], arr[max_stone_index]
    return arr.pop()

arr = [2,7,4,1,8,1] # 1
print(last_stone_weight(arr))
