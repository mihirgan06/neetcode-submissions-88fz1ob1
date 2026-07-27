"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
            Given an array of meeting time interval objects
            find the mun number of rooms requried to schedule all meetings without conflicts

            intervals = [(0,40),(5,10),(15,20)]
            output = 2
            start by sorting if we see ovrlap we increment count


        '''
        if not intervals:
            return 0

        intervals.sort(key = lambda i: i.start)
        rooms = []

        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, interval.end)

        return len(rooms)

        