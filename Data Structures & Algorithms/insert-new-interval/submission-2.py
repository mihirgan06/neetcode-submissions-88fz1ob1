class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            given non-overlapping intervals, intervals[i] = [start_i, end_i]
            represents the start and end time of the ith interval
            INTERVALS IS INITIALLY SORTED BY start_i
            We are given another additional interval = start, end

            insert the new interval into intervals so that intervals is still sorted in ascending order by start time and doesn't have any overlapping intervals
            intervals = [[1,3],[4,6]], newInterval = [2,5]
            [1,6]]

            [2,5] is overlapping with the intervals array

            so we merge all three into [1,6]


            intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

            no overlap, so just insert it at the right spot


            we can start with res = the first interval
            then loop through the rest and do the same check as merge intervals

            if the new interval start time is > end time of any interval AND the end time of the new interval is < end time of the next interval


            3 cases:
            1. end < new_start 
                we just append the normal interval, the new interval might come later/merge later
            2. start > new_end
                [9,10] vs [6,7]
                [6,7] should come before [9,10]
            3. MERGE REQUIRED:
                the case here start <new_start and end >= new_start
                newInteval[0] = min of the new interval start time and start
                newInterval[1] = max of the two end times




        '''
        res = []
        for start, end in intervals:
            new_start = newInterval[0]
            new_end = newInterval[1]
            #current inteval comes fully before new interval keep moving forward
            if end < new_start:
                res.append([start, end])
            elif start > new_end:
                #append the new interval and then shift the new interval so now were processing [9, 10]
                res.append(newInterval)
                newInterval = [start, end]
            else:
                #merge required
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res



            

        
        