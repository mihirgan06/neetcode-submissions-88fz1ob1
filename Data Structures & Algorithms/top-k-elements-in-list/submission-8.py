class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        '''
            given an integer array nums and integer k return the k most frequent elemnts within the array

            nums = [1,2,2,3,3,3], k = 2

            2 shows up 2 times, 3 shows up 3 times


            create a bucket sort array

            - create an array with the number of elements
            - if i have nums where the elements are 1,2,3

            - you would start with empty slots for 1 2 and 3


            then we would store counts for each elements
            
            goal: 
            - index = frequency
            - value = elements appearing frerquency times
            
        '''

        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
            #store counts for each number in nums

        bucket_sort = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            bucket_sort[count].append(num)
        res = []
        for i in range(len(bucket_sort) -1, -1, -1):
            for num in bucket_sort[i]:
                res.append(num)
                if len(res) == k:
                    return res

            



        