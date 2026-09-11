class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            Given an array of intervals, where intervals[i] = [start_i, end_i] merge all overlapping intervals

            return an array of the non-overlapping intervals that cover all intervals in the inpuy

            intervals = [[1,3],[1,5],[6,7]]

            return : [[1,5],[6,7]]
            take the first bound from the initial array, and the last bound from the interval that stretches further

            iterate through intervals 

            check whether the last interval goes past the start of the next interval
        '''
        res = []
        intervals.sort(key = lambda pair: pair[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = res[-1]


            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])

            # no overlap
            else:
                res.append(curr)

        return res
                
                

        