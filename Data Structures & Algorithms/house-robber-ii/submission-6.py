class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            you are given an integer array nums, nums[i] = amount of money the ith house has

            houses are arranged in curcle
            first and last house are neighbors

            cannot rob two adjacent houses because the security system will auto alert police

            return the max amount of money you can rob without alerting the police

            nums = [3,4,3]
                4
            /       \
            3  ---   3

            nums = [2,9,8,3,6]

            so same rules for adjacency follow but theres an additional condition that the first and last house cannot be selected in the same path


            we need to find the max includoing the start and including the end

            

        '''
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        
        dp[1] = nums[0]
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        dp2 = [0] * n

        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
        return max(dp[n - 1], dp2[n - 1])
        




        