"""

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:

Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:

Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:

Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..

"""
from collections import deque
# this is wrong.
def collision_uhoh(asteroid_array):
    is_still_colliding = True
    index = 0
    while (is_still_colliding):
        is_still_colliding = False
        i = index
        while i < len(asteroid_array):
            if i != len(asteroid_array) - 1:
                # check if the two asteroids will collide by looking to see
                    # if the they have different signs.
                if asteroid_array[i] > 0 and asteroid_array[i+1] < 0:
                    if abs(asteroid_array[i]) ==  abs(asteroid_array[i+1]):
                        index+=2
                    else:
                        collision = max(asteroid_array[i], asteroid_array[i+1])
                        # if they do compute their difference and add the new element
                            # as the second element that was compared so that
                            # it can interact with the remaining asteroid of the array
                        asteroid_array[i+1] = abs(collision)
                        index+=1
                        # set collision to true to show that collisions are still happening.
                        is_still_colliding = True
            i+=1
    return asteroid_array[:-index] if index != 0 else asteroid_array


asteroids = [-2, -1, 1, 2] # [-2, -1, 1, 2]
# asteroids = [8, -8] # []
# asteroids = [5, 10, -5] # [5, 10]
# print(collision_uhoh(asteroids))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None

class Linkedlist:
    def __init__(self,asteroids):
        self.head = None
        self.tail = None
        for asteroid in asteroids:
            self.add_node(asteroid)

    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        elif self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
            self.tail.last = self.head
        else:
            new_node.last = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def replace_data(self, index, data):
        count = 0
        node = self.head
        while node:
            if count == index:
                node.data = data
                return True
            node = node.next
            count+=1
        return False

    def remove_node(self, index):
        count = 0
        node = self.head
        while node:
            if count == index:
                node.last.next = node.next
                node.next.last = node.last
                return True
            node = node.next
            count+=1
        return False

asteroids = [10, 2, -5] # [10]

def collision(asteroid_array):
    # an array of asteroids that are on the left and moving right
    colliders = []
    collider_index_array = []
    for i, asteroid in enumerate(asteroid_array):
        # a potential asteroid from colliders array
        collider = None
        # if the current element is not None
        if asteroid:
            # if the current asteroid is moving right
                # add it to the colliders array
            if asteroid > 0:
                colliders.append(asteroid)
                collider_index_array.append(i)
            # else if it's moving left
                # check if there are any asteroids moving right.
                # and if there are, pop the the closest one.
            else:
                if len(colliders):
                    collider = colliders.pop()
                    collider_index = collider_index_array.pop()
            # if we have a collision (if collider is not None
                # check if the current asteroid against the collider
            while collider and asteroid:
                # if they're of equal size. set everything to None
                if abs(collider) == abs(asteroid):
                    asteroid_array[collider_index] = None
                    asteroid_array[i] = None
                    collider = None
                    asteroid = None
                # if the right side asteroid is larger.
                    # set the asteroid to None
                elif abs(collider) > abs(asteroid):
                    asteroid_array[i] = None
                    asteroid = None
                # if the left side asteroid is larger.
                    # set the collider to None
                    # and grab the next one from the stack.
                else:
                    asteroid_array[collider_index] = None
                    collider = None
                    if len(colliders):
                        collider = colliders.pop()
                        collider_index = collider_index_array.pop()
                print(collider,asteroid)

    return [asteroid for asteroid in asteroid_array if asteroid != None]


print(collision(asteroids))
