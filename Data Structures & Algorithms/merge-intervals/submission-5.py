class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            givena n array of intervals
            intervals[i] = [start_i, end_i], merge all overlapping intervals
            return the array of non-overlapping intervals that cover all intervals in the input

            intervals = [[1,3],[1,5],[6,7]]
            [[1,5],[6,7]]
            the entirety of interval 1 is sored in interval 2
            sort by end times


            if the start time of the interval were at is <= prev end we can merge by changing the max to the max of the res end and the end of the interval

            
        '''
        res = []
        intervals.sort(key = lambda pair: pair[0])
        res.append(intervals[0])
        #start with intervals[0] in the res array
        for start, end in intervals[1:]:
            prev_end = res[-1][1] #end time of last interval in res

            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res
                
            


        