"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
            given: meeting time interval objects with start and end times
            intervals = [(0,30),(5,10),(15,20)]

            (0,30) goes tooo far so theres no room to attend the next two intervals

            intervals = [(5,8),(9,15)]
            true, the first interval finishes before the next


            Approach:
            start by sorting the intervals by start time
            if the end time of the interval were at > the next interval return false
            continue iterating
        '''
        intervals.sort(key = lambda i: i.start)


        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev.end > curr.start:
                return False
        return True
