class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            given an array of intervals where intervals[i] = [start_i, end_i]
            return the min mumber of intervals you need to remove to make the rest of the intervals non-overlapping


            intervals = [[1,2],[2,4],[1,4]]
            1 if you remove [1,4] its not overlapping
            intervals = [[1,2],[2,4]]

            0 no overlap

            we can sort by end time?

            [[1,2], [1,4], [2,4]]
            start time of [1,4] <= [2,4] thats an overlap remove 1 incrment count by 1




        '''

        intervals.sort(key = lambda pair: pair[1])
        count = 0

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
            else:
                prev_end = end
        return count
            
        