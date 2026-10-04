class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            given an array of intervals, intervals[i]  [start_i, end_i]
            merge all overlapping intervals
            and return an array of the non-overlapping intervals
            intervals = [[1,3],[1,5],[6,7]]

            [[1,5],[6,7]]

            end time of the first interval is <= end time of the next interval
            start time of the next interval is <= end time of the prev interval

            intervals = [[1,2],[2,3]]
            [[1,3]]
            end time of the next interval is <= start time of the prev interval
            take the max of the two end times as the res end time

            Start by sorting the intervals
            let res = the first interval
            then iterate through the remaining intervals and comapre the end times
            if the start time is <= end time of prev interval take the max of the two interval end times and make it the new res end itme
        '''

        res = []
        intervals.sort(key = lambda pair: pair[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res
        








        