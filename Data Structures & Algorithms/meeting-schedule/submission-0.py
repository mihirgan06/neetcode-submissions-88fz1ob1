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
            Given an array of meeting time interval objects]
            determine if a person could add all meetings to their schedule w/o conflicts

            intervals = [(0,30), (5,10), (15,20)]
            output = false
            0,30 conflicts with both the later intervals


           intervals = [(5,8),(9,15)]
           output = True
           no overlap here so true

        '''
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev.end > curr.start:
                return False
        return True
             


            
            

