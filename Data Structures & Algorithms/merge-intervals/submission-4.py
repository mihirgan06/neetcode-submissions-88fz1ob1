class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''

            given an array of itnervals, intervals[i] = [start_i, end_i]
            merge all overlapping intervals

            return an array of the non-overlapping intervals that cover all the intervals in the input


            intervals = [[1,3],[1,5],[6,7]]

            [[1,5],[6,7]]

            end time of the first interval is < end time of the next interval so merge those two and the end time of the first interval >= start time of the next interval

            intervals = [[1,2],[2,3]]

            [[1,3]]

            end tim of the first interval is >= start time of the next interval and < end time of the next interval 



        '''
        res = []
        intervals.sort(key = lambda pair: pair[0]) #sort based on start time
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res
        