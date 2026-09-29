"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
            given an array of meeting time itnerval objects with start and end itmes


            find the min numebr of rooms required to schedule all meetings without any conflicts

            intervals = [(0,40),(5,10),(15,20)]

            if there is a conflict ie end time for the previous interval > start time for an interval we need
            an additional meeting rooms

            one meeting room for 0,40
            additional meeting room for (5,10) and (15,20)

            



        '''
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)
        heap = []
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)




        