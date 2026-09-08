class Solution:
    from collections import defaultdict

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            given an array of integers nums and integer target
            return i and j such that nums[i] + nums[j[ == target and i != j
            exactly one pair and j




            [3,4,5,6] target = 7

            [0,1]
            when at i = 0, we have value 3, and we know the compliment of 3 here is 4 so we
            are looking for the index where 4 exists

            we are guaranteed this exists if we choose 3



        '''
        seen = {}
        res = []
        
        for i, num in enumerate(nums):
            comp = target - nums[i]

            if comp in seen:

                res.append(seen[comp])
                res.append(i)
                return res
            if nums[i] not in seen:
                seen[nums[i]] = i
        return res










        