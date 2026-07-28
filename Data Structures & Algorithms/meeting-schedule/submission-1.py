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
            Given an array of meeting times with start and end times, determine if aperson can add all meetings w/o conflicts

            intervals = [(0,30), (5,10), (15,20)]
            0,30 continues past the first meeting so instantly return false, no need to check w next paur

            so you can just sort then check adjacent meeting times

        '''
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev.end > curr.start:
                return False
        return True
            
