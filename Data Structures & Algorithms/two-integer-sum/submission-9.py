class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            given an array nums and an integer target, return indices i and j such that
            nums[i] + nums[j] == target and i != j

            TWO differnet indices such that nums[i] + nums[j] = target

            nums = [3,4,5,6], target = 7

            process nums[0] 
            compliment = 7 - 3 = 4
            so we look for where 4 is in the array, but we need this lookup in O(1)
            so we can map the value to the indices
        '''



        index_map = defaultdict(int)


        for i in range(len(nums)):
            index_map[nums[i]] = i
        

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement not in index_map.keys():
                continue
            if complement in index_map and index_map[complement] != i:
                return [i, index_map[complement]]
            
        









        