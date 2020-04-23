
"""City Rain (intermediate) - Imagine you are given an array of positive integers
that represent the height of buildings in a 2D city.
Each night rain falls on the city and the water pools between the buildings.
Write a function that takes in the array and outputs the amount of water that
pools. E.g.,  [4, 2, 3, 4] => 3,  [3, 5, 2, 3] => 1"""

"""
   4 2 3 3  4 2 3 3 => 5
   []      []
   []  [][][]  [][]
   [][][][][][][][]
   [][][][][][][][]

   start iterating over the array
   as you iterate over the array, keep track of the maximum number seen
   and the

   what we need:
       two maximum numbers
       the numbers that occur in-between those two maximums

       the smaller of the two maximum numbers is the limiting factor.
       iterate over the subset of numbers that fall between the maximums.
            compute the difference between the smaller maximum number and the current num in the subset
            add the difference to the amount of rainfall

    algo:
        iterate over array:
            at num compare to max_num

                if num is larger than max_num and there are no items in run_array
                discard max_num and set max_num to num

                if num is larger than or equal to max_num and there are items in the run_array
                    iterate over the run and add to the total rainfall by computing the difference between each number in the run_array when compared to the smaller max_num
                    empty run_array
                    set the max_num to be the current num

                if num is smaller than max_num add item to run_array

                if array end has been reached and numbers are in the run, find the max num in the run and compute the rain fall of that subset of the run
                    set the new max_num to be that num and remove the subset from the run recurse on the run array computing the rainfall between each maximum that remains until no nums remain in the run.


"""

def city_rain(array):
    max_v = float("-inf")
    run = []
    for i, num in enumerate(array):
        temp = max_v
        max_v = max(max_v, num)
        if max_v != temp and i != 0:

            run = [max_v]


"""
[4, 2, 3] => 1,

[]
[]W []
[][][]
[][][]

[3, 5, 2, 3, 4] => 3

  []
  []W  W[]
[][]W [][]
[][][][][]
[][][][][]

when does pooling occur?

needs to be a deficit of 3<=
2 higher ends with 1 or more lower numbers
pool = lowest, not highest

two ends = the lowest number is the one that matters
depth of pool = the height of the lowest end / high point - the height of the current column

ends (two number)
the lowest end
height of the column as we iterate (for pools/dips)


iterate through the array
if number1 > number2:
store number1 as a key in dict

if number is greater than or equal to that key or if we've reached the end of the array
iterate through values and find max value that is the lower tower
iterate through the values of that key and compute score based on max value in the value

if we find number is less than or key
store number as value

"""
def city_rain(array):
    max_v = float("-inf")
    run = {}
    total_water = 0
    for i, num in enumerate(array):
        if i == 0:
            max_v = num
        else:
            if max_v >= num:
                if max_v in run:
                    run[max_v].append(num)
                else:
                    run[max_v] = [max_v]
            else:
                lower_tower = max(run[max_v])
                for pool_section in run[max_v]:
                    total_water += lower_tower - pool_section
                max_v = num
                run = {}
                run[max_v] = [max_v]
                print(max_v)
    lower_tower = max(run[max_v])
    for pool_section in run[max_v]:
        total_water += lower_tower - pool_section

    return total_water

array = [4, 2, 3]
array = [3, 5, 2, 3, 4]
print(city_rain(array))
