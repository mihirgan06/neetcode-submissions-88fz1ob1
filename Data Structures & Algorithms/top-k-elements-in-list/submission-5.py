class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Given an array nums and an integer k, return the k most frequent elements within  the array

            nums = [1,2,2,3,3,3], k = 2

            2 most frequent elements are 2 and 3
            2 appears 2 times, 3 appears 3 times
            nums = [7,7], k = 1
            7 is the only element so it appears the most

            bucket sort:
            Array of all the frequencies from 1 to n
            freq stroes the frequencies of each number in nums
            [1,2,2,3,3,3]
            1: 1
            2: 2
            3: 3

        '''
        
        freq = defaultdict(int)
        res = []
        for i, num in enumerate(nums):
            freq[num] += 1
        

        n = len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        




        


            







        