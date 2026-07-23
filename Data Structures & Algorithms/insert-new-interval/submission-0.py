class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            intervals[i] = [start_i, end_i] represents the start and end time of the ith interval
            intervals are initially sorted in ascending order by start_i


            newInterval = [start, end]
            Insert newInterval into intervals such that intervals is sorted by asc order
            no overlapping intervals, merge the overlapping intervals if needed
            return intervals


            
        intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output = [[1,6]]
        [2,5] overlaps with bioth intervals so it merges into the larger full interval

        intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        - no overlap

        [[1,2], [3,5], [6,7], [9,10]]

        O(n) time

        - loop through intervals compare the end value for each interval with our start of new_intervakl
        '''
        res = []

        for i in range(len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append(newInterval)
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res
            

