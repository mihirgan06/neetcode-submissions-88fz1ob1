class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# basically create a hashmap where each key contains the prior key's values for addition
# this would look like
# [3,4,5,6], target = 7
# 3 -> 3, 7, 8, 9
# 4 -> 3, 4, 9, 10
# 5 -> 3, 4, 5, 11

    #create a hashmap with the number as a key and indicie as value
        indicies = {}
        for i, n in enumerate(nums):
            indicies[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if(diff in indicies and indicies[diff] !=i):
                return [i, indicies[diff]]
        return []