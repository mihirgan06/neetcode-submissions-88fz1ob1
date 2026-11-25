class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            given array of integers nums and an integer target
            return the indices i and j such that nums[i] + nums[j] == targert and i != j
            assume every input has exactly one pair of indices that satisfy

            [3,4,5,6] target = 7
            [0,1] indices

            hold a hashmap of integer type that has the compliment for each number in nums to get to the target


        '''
        compliment_map = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in compliment_map:
                return [compliment_map[compliment], i]
            compliment_map[num] = i