class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
            given an array of positive nums and target
            return the min length of a subarray whose sum is >= target 
            if no subarray return 0
            we shift the window when our running sum >= target

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


