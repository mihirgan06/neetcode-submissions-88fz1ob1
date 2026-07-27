class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            Given an array of intervals, where intervals[i] = [start_i, end_i]
            return the min number of intervals ypu need to remove to make the rest of the intervals non-overlapping

            intervals = [[1,2],[2,4],[1,4]]
            output = 1

            intervals = [[1,2],[2,4]]
            output = 0
            
            basically we count the number of overlappign intervals
        '''
        count = 0
        intervals.sort(key = lambda pair: pair[1])
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
            else:
                prev_end = end
        return count
            
        