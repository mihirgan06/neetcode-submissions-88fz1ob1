from collections import Counter
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        EX: [1.2.2, 3,3,3,] k = 2
        freq = {1: 1, 2: 2, 3: 3}
        GOAL: O(N)
        Iterate through the freq map (suppose the values), each time find the max count
        decrement k
        while k > 0 keep going
        update in a result list\


        HOWEVER, THIS APPROACH IS O(N^2) --> BUCKET SORT
        '''


        count = Counter(nums)
        res = []

        freq = [[] for i in range(len(nums) + 1)] #index is freq or count, value is gonna be the values whoich appear i times
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        