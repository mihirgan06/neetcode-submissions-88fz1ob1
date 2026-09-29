class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            given an array of intervals where intervals[i] = start_i, end_i

            return the min number of intervals you need to remove to make the rest of the intervals nonoverlapping

            intervals = [[1,2],[2,4],[1,4]]

            sort the intervals in increasing order by start time

            [[1,2], [1,4], [2,4]]

            nonoverlapping would become --: [1,2],[2,4]

            intervals = [[1,2],[2,4]]

            0




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




        