"""
A frog is crossing a river. The river is divided into x units and at each
unit there may or may not exist a stone.
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1
unit.

If the frog's last jump was k units, then its next jump must be either k - 1,
k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping
1 unit to the 2nd stone, then 2 units to the 3rd stone, then
2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as
the gap between the 5th and 6th stone is too large."""


# Initially, the frog is on the first stone and assume the first jump must be 1
# unit.
#
# If the frog's last jump was k units, then its next jump must be either k - 1,
# k, or k + 1 units. Note that the frog can only jump in the forward direction.

stones = [0,1,3,5,6,8,12,17] # true
# stones = [0,1,2,3,4,8,9,11] # false

 # not working
def frog_jump(stones):
    def recur(i,k):
        print(stones[i], stones[i-k], k)
        if i < 0 or (i-k) < 0:
            return False
        if stones[i] - stones[i-k] <= k or i == 0:
            # frog must jump on the last stone to cross
            if i == len(stones)-1:
                return True
            # cannot jump over last stone
            elif i > len(stones)-1:
                return False
            else:
                return recur(i+k,k) or recur(i+k+1,k+1) or recur(i+k-1,k-1)
        else:
            return False

    return recur(0,1)

print(frog_jump(stones))
