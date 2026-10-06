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
            given: array of meeting time interval objects with start and end times

            starti < endi
            find the min number of rooms required to schedue all meetings without any conflcits

            intervals = [(0,40),(5,10),(15,20)]

            0                   40
            ---------------------
                5---10. 15--20
        time, meeting room becomes available
        intervals = [[0,30], [5,10], [15,20]]

        (0, +1)
(30, -1)

(5, +1)
(10, -1)

(15, +1)
(20, -1)

(0, +1)
(5, +1)
(10, -1)
(15, +1)
(20, -1)
(30, -1)
time 0:  rooms = 1
time 5:  rooms = 2   <- max
time 10: rooms = 1
time 15: rooms = 2
time 20: rooms = 1
time 30: rooms = 0



        
        '''
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort(key = lambda x: (x[0], x[1]))
        #sprt by time and number of rooms
        #start means add 1 for the count for the meeting room
        #end means usbtract 1 as a room becomes free

        rooms = 0
        max_rooms = 0

        for time, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        return max_rooms


        