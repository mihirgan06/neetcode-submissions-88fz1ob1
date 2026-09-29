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
            given an array of meeting time itnerval objects consisting of start and end times


            [[start, end], [start, end]... start < endi]

            determine if a person could add all meetings without conflicts


            intervals = [(0,30),(5,10),(15,20)]

            overlap so return false

            sort by start time

            iterate through intervals start < prev_end --> false





        '''
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if curr.start < prev.end:
                return False
        return True
            


        
