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
            given an array of meeting times
            consisting of stgart and end times find the min nmber of rooms required to schedule all meetings without conflicts


            intervals = [(0,40),(5,10),(15,20)]

            we need 1 meeting room for (0,40)
            and then amnother meeting room for (5,10)
            we can then use the same meeting room for (15,20)


            number of rooms should be incremented when the end time of the prev interval exceeds the start time



            we cant jsut compare to the previous interval, we need to find out of all currently occupied rooms which finishes first
        '''
        heap = []
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)

        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)
            
            
        