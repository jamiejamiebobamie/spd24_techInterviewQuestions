
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
