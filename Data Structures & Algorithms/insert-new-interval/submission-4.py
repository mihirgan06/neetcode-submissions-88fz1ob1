class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            Given: array of non-overlapping intervals
            intervals[i] = [start_i, end_i]
            newInterval = [start, end]
            insert newInterval into intervals such that intervals is sorted in ascending order by start_i

            intervals = [[1,3],[4,6]], newInterval = [2,5]
            newstart = newinterval[0]
            newend = newinterval[1]

            3 cases:
            1. we have to merge intervals
                start < prev end

            2. we paste the new interval immediately
            3. we copy over the existing interval before the newinterval
                we set the newinterval to the existing
            
        '''
        
        res = []
        for start, end in intervals:
            newStart = newInterval[0]
            newEnd = newInterval[1]
            if end < newStart:
                res.append([start, end])
            elif newEnd < start:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(newStart, start)
                newInterval[1] = max(newEnd, end)
        res.append(newInterval)
        return res
                

                

        