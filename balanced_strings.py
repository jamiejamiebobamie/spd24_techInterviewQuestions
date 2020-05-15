"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.


Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLL RLL", since each substring contains an equal number of 'L' and 'R'


"""
# in progress...  not working
def return_max_balanced_groups(string):
    test = []
    curr = None
    max_nums = 0
    # "RL RRRLLRLL"
    for char in string:
        # if test has items and the items are of an even quantity...
        if len(test) and not len(test)%2:
            lower_index = len(test)/2 - 1
            upper_index = len(test)/2
        test.append(char)

    #     if curr == None:
    #         curr = char
    #         test.append(char)
    #     elif char == curr:
    #         test.append(char)
    #     elif char != curr:
    #         if len(test) > 1:
    #             test.pop()
    #         else:
    #             max_nums += 1
    #             curr = None
