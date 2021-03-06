"""Wed Jan 29 Activity: Simplify the Problem
Simplify, Simplify, Simplify!
Come up with at least 3 different ways to simplify the problem given below,
then share your ideas with other students and borrow their ideas that you think
would be helpful.

Create a Plan
Then create a plan for how you’ll solve the problem from the absolute simplest
possible version as step 1, then remove one of the simplifications in step 2,
then another in step 3, and finally remove all simplifications so you are
solving the full version of the problem in your final step. DO NOT attempt to
solve the full version of the problem right away.
The goal of this activity is to break the problem down into smaller, simpler
steps to create an incremental path from the simplest version to the full
problem. Practicing this will help you during real interviews, especially when
you hear a new problem and think to yourself “OMG this is hard!” – This is to
develop a strategy for how to move past those thoughts.

New Problem: Twitter Follow Suggestions
You’re working an internship at Twitter and are tasked to improve suggestions
for accounts to follow, which already works great for established accounts
because it uses content from your tweets and other accounts you follow to
suggest new ones. However, when a new user signs up none of this information
exists yet, but Twitter still wants to make some follow suggestions. Your team
asked you to implement a function that accepts a new user’s handle and an array
of many other users’ handles, which could be very long – Twitter has over 330
million active accounts! You need to calculate a similarity score between a
pair of handles by looking at the letters each contains, scoring +1 for each
letter in the alphabet that occurs in both handles but scoring –1 for each
letter that occurs in only one handle. Your function should return k handles
from the array that have the highest similarity score to the new user’s handle.

Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

Possible Simplifications
The text below is white to hide solutions so those who missed class can
make full use of the activity. – Once you’ve come up with your own ideas,
select the text below to view the list.
Find only 1 handle with the highest similarity, then later try to find 2, and
then k handles.
Implement only a similarity score helper function, then later use it to find
similar handles.
When calculating similarity scores, only count +1 for matching letters at first,
then later include –1 for non-matching letters.
Make letter matching case sensitive at first, then later make matching case
insensitive.
Generate more simplifications and add them here!"""

# a max/min heap would be really helpful to know how to use right about now...

# Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
# suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

"""SIMPLIFICATION #1"""
# i solve it by finding the closest
def find_closest_handle(user_handle, handles_array):
    """Finds the closest handle to the user."""

    user_handle_chars = set()
    for char in user_handle:
        user_handle_chars.add(char)

    max_score = float("-inf")
    max_handle = ""
    for handle in handles_array:
        score = 0
        for char in handle:
            if char in user_handle_chars:
                score += 1
            else:
                score -= 1
        temp = max_score
        max_score = max(score,max_score)
        if temp != max_score:
            max_handle = handle

    return max_handle

print(find_closest_handle('iLoveDogs', handles))

handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']

"""SIMPLIFICATION #2"""
# if k > handles_array, i return it without worrying about who the closest names are.
def find_closest_handles(user_handle, handles_array, k):
    """Finds the closest handles (k) to the user's handle."""

    result = []

    if k > len(handles_array):
        return handles_array

    user_handle_chars = set()
    for char in user_handle:
        user_handle_chars.add(char)

    handle_scores_dict = {}
    for handle in handles_array:
        score = 0
        for char in handle:
            if char in user_handle_chars:
                score += 1
            else:
                score -= 1

        if score not in handle_scores_dict:
            handle_scores_dict[score] = [handle]
        else:
            handle_scores_dict[score].append(handle)

    while len(result) < k:
        max_key = max(handle_scores_dict.keys())
        max_key_handles = handle_scores_dict[max_key]
        i = 0;
        while len(result) < k and i < len(max_key_handles):
            handle = max_key_handles[i]
            result.append(handle)
            i += 1
        del handle_scores_dict[max_key]
    return result

print(find_closest_handles('iLoveDogs', handles, 3))
print(find_closest_handles('iLoveDogs', handles, 10))


"""SOLVING IT!!"""
def find_closest_handles_yay(user_handle, handles_array, k):
    """Finds the closest handles (k) to the user's handle."""

    result = []

    user_handle_chars = set()
    for char in user_handle:
        user_handle_chars.add(char)

    handle_scores_dict = {}
    for handle in handles_array:
        score = 0
        for char in handle:
            if char in user_handle_chars:
                score += 1
            else:
                score -= 1

        if score not in handle_scores_dict:
            handle_scores_dict[score] = [handle]
        else:
            handle_scores_dict[score].append(handle)

    while len(result) < k and len(handle_scores_dict) != 0:
        max_key = max(handle_scores_dict.keys())
        max_key_handles = handle_scores_dict[max_key]
        i = 0;
        while len(result) < k and i < len(max_key_handles):
            handle = max_key_handles[i]
            result.append(handle)
            i += 1
        del handle_scores_dict[max_key]
    return result

print(find_closest_handles_yay('iLoveDogs', handles, 10))
