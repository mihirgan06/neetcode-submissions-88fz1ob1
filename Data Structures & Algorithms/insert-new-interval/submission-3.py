class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            Given:
            - array of non-overlapping intervals:
            intervals[i] = start_i, end_i
            represents the start and the end time of the ith interval

            intervals is sorted in ascending order by start_i

            Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i


            intervals = [[1,3],[4,6]], newInterval = [2,5]

            we check if the start time for the new interval is <= to any of the current intervals
            [[1,3],[4,6]]
            2 <= 3
            so merge with the larger of the end times

            [[1,5],[4,6]]
            but then 4 is less than 5 so merge those two as well

            so after we merge reassign the new interval to the new start end

            intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

            6 > 2
            6 > 5






            
        '''


        res = []

        for start, end in intervals:
            new_start = newInterval[0]
            new_end = newInterval[1]
            #the existing interval should come first the entire interval finishes before the new interval
            if end < new_start:
                res.append([start, end])
            elif start > new_end:
                res.append(newInterval)
                newInterval = [start, end]


            else:

                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res
            
            
            



            



        