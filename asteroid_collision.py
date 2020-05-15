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

# this works.
# O(n) time complexity.
# O(1) space.
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
                    # set the (left) asteroid to None
                elif abs(collider) > abs(asteroid):
                    asteroid_array[i] = None
                    asteroid = None
                # if the left side asteroid is larger.
                    # set the collider to None
                    # and grab the next one from the stack.
                else:
                    asteroid_array[collider_index] = None
                    collider = None
                    if colliders:
                        collider = colliders.pop()
                        collider_index = collider_index_array.pop()

    return [asteroid for asteroid in asteroid_array if asteroid != None]


asteroids = [-2, -1, 1, 2] # [-2, -1, 1, 2]
asteroids = [8, -8] # []
asteroids = [5, 10, -5] # [5, 10]
# asteroids = [10, 2, -5] # [10]

print(collision(asteroids))
