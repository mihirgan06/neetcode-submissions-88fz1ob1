class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            O(n) time + Memory --> bucket sort
            Each number count the number of occurances
            Go through input arrray count occurances, map to index and add that value
            [1,1,1,2,2,100]
            i      0 1 2 ... 100
            count    3 2.    1


            INSTEAD
            make the index = COUNT of the values
            and then the VALUES is a list of vlaues which appears index times

            0 1     2    3      4 5 6
              [100] [2]  [1,2]
            
            FOR THE TOP K VALUES
            - we start at the right end of the table
            - here, if 1 occurs 3 times, 2 occurs once, we would return 1 and 2 for top 2 elements
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #valyue = list of values which occur n amt of times
        #we want the number of empty arrays to be the size of the current nums array

        #counmting how many times each number appears
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

