"""Given an array of meeting time intevls consisting of start and end times
    [[s1,e1],[s2,e2], etc] find the minimum # of conference rooms required.

sample
    input: [[0,30],[5,10],[15,20]]
    output: 2

"""

def min_rooms(meeting_times):
    # put all of the start and end times in a dictionary
    # with start times as the keys
    # and ending times as values (as an array in case of duplicate start times).
    starting_times = {}

    # add the times to the 'starting_times' dict as well as find when the last meeting is over.
    last_meeting_time_end = 0
    for start,end in meeting_times:
        last_meeting_time_end = max(last_meeting_time_end, end)
        if start not in starting_times:
            starting_times[start] = [end]
        else:
            starting_times[start].append(end)


    ending_times = {}
    most_rooms = 0
    # iterate through all of the minutes from now until the conclusion of the last meeting.
    for minute in range(last_meeting_time_end+1):
        # compute the sum of all of the array lengths of the ending_times.values()
        # as this signifies the total # of meetings in progress.
        sum = 0
        for values in ending_times.values():
            sum+=len(values)
        most_rooms = max(sum,most_rooms)

        # if the dict is not empty (if there are meetings in progress)
        if len(ending_times) != 0:
            # if the current minute is an end_time for a meeting.
            # remove it from the dictionary, regardless of which start_time
            # (if several) started the meeting, all meetings with that end time
            # are now over.
            if minute in ending_times:
                del ending_times[minute]
        # finally check if the current minute is in the meeting times
        # 'starting_times' dictionary and if it is, add the end_time to the
        # ending_times dict to begin the meeting.
        if minute in starting_times:
            meeting_end_times_for_that_start_time = starting_times[minute]
            for end_time in meeting_end_times_for_that_start_time:
                if end_time not in ending_times:
                    ending_times[end_time] = [minute]
                else:
                    ending_times[end_time].append(minute)

    return most_rooms


# arr = [[0,30],[5,10],[15,20]]
# arr = [[7,10],[2,4]]
arr = [[3,10],[5,6],[4,6]]

# O(n+l) runtime n being the number of meeting times
# and l being the range of 0 to the last meeting's
# end time. O(n) storage.
print(min_rooms(arr))
