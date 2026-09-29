class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            given an array of integers nums with n + 1 integers

            each int in nums is in the range [1,n]
            iterate through the nums array if nums in seen alr return the num thats in seen
        '''
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])
        return -1

        