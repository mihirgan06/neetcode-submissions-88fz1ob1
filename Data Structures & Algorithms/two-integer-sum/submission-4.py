class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            Return indices i and j such that nums[i] + nums[j] == target
            i cannot = j
        
        '''
        from collections import defaultdict

        my_map = defaultdict(int)
        res = []
        for i, num in enumerate(nums):
            #first compute complement
            complement = target - nums[i]
            #if comp is in the map then return that with the index
            if complement in my_map:
                return [my_map[complement], i]
            #set the value = to an index
            my_map[num] = i
        return res

        