#############
#Problem - 

# Your company built an in-house calendar tool called HiCal. You want to
# add a feature to see the times in a day when everyone is available.
#
# To do this, you'll need to know when any team is having a meeting. In
# HiCal, a meeting is stored as tuples of integers (start_time,
# end_time). These integers represent the number of 30-minute blocks
# past 9:00am.

# For example:

# (2, 3) # meeting from 10:00 - 10:30 am
# (6, 9) # meeting from 12:00 - 1:30 pm

# Write a function merge_ranges() that takes a list of meeting time
# ranges and returns a list of condensed ranges.
#
# For example, given:
#
test1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return:

soln1 = [(0, 1), (3, 8), (9, 12)]

# Do not assume the meetings are in order. The meeting times are coming
# from multiple teams.

# Write a solution that's efficient even when we can't put a nice upper
# bound on the numbers representing our time ranges. Here we've
# simplified our times down to the number of 30-minute slots past 9:00
# am. But we want the function to work even for very large numbers, like
# Unix timestamps. In any case, the spirit of the challenge is to merge
# meetings where start_time and end_time don't have an upper bound.

################


def merge_ranges(meetings):

    # Merge meeting ranges
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings)
    print(meetings)
    pdl = [meetings[0]]
    meetings = meetings[1:]
    for (nstart, nend) in meetings:
        (start, end) = pdl[-1]
        if nstart <= end:
            if end <= nend:
                end = nend
            pdl[-1] = (start, end)
        else:
            pdl.append((nstart, nend))
    print(pdl)
    return pdl
