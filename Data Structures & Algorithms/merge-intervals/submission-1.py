class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            Array of intervals where intervals[i] = [start_i, end_i]
            merge all overlapping intervals and return an array of nonoverlapping intervals that cover all intervals in the input

            intervals = [[1,3],[1,5],[6,7]]
            1,5 consumes 1,3

            ntervals = [[1,2],[2,3]]
            the entire interval of 2,3 and 1,2 can be summarized with 1,3
            we want to sort so that all overlapping intervals are side by side

        '''
        intervals.sort(key = lambda pair: pair[0])

        output = intervals[0]
        for start, end in intervals:
            #we start with the first interval in output
            #so for intervals = [[1,3],[1,5],[6,7]], if output starts as [1,3] 
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output
                
            



        