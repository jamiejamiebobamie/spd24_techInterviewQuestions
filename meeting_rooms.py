"""Given an array of meeting time intevls consisting of start and end times
    [[s1,e1],[s2,e2], etc] find the minimum # of conference rooms required.

sample
    input: [[0,30],[5,10],[15,20]]
    output: 2

"""


def min_rooms(meeting_times):
    # put all of the start and end times in a dictionary
    # with start times as the keys
    # and ending times as the value.
    time_lookup = {}

    # add the times to the 'time_lookup' dict as well as find when the last meeting is over.
    last_meeting_time_end = 0
    for start,end in meeting_times:
        last_meeting_time_end = max(last_meeting_time_end, end)
        time_lookup[start] = end

    ending_times = []
    most_rooms = 0
    # iterate through all of the minutes from now until the conclusion of the last meetin.
    for minute in range(last_meeting_time_end+1):
        # compute the max number of rooms given the current state
        # of the ending_times array which signifies the total #
        # of meeting in progress currently.
        most_rooms = max(len(ending_times),most_rooms)
        # peek at the top of the ending time stack
        # (this is the problem with my solution and why it will not work,
        # and if it does work ... why???)
        if len(ending_times) != 0:
            last_index_of_array = len(ending_times)-1
            top_of_ending_times_stack = ending_times[last_index_of_array]
            # if the meeting's ending time is the current minute,
            # pop it from the meeting ending_times array
            if top_of_ending_times_stack == minute:
                ending_times.pop()
        # finally check if the current minute is in the meeting times
        # 'time_lookup' dictionary and if it is at the endingtime to the
        # ending_times array to beign the meeting.
        if minute in time_lookup:
            meeting_end = time_lookup[minute]
            ending_times.append(meeting_end)

    return most_rooms


arr = [[0,30],[5,10],[15,20]]
arr = [[7,10],[2,4]]
print(min_rooms(arr))
# it works...
