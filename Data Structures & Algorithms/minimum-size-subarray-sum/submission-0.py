class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
            given an array of positive integers nums and a positive integer target
            return the minimal length of a subarray whose sum is greater than or equal to target


            return 0 if not possible

            target = 10, nums = [2,1,5,1,5,3]

            start l at 2
            keep moving r till we compute a running sum = target
            2 + 1 + 5 + 1 + 5 > 10
            slide l forward
            1 + 5 + 1 + 5 > 10
            slide l forward
            5 + 1 + 5 = 3
        '''
        l = 0
        min_len = float('inf')
        running_sum = 0
        for r in range(len(nums)):
            running_sum += nums[r]
            while running_sum >= target:
                min_len = min(min_len, r - l + 1)
                running_sum -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0
        