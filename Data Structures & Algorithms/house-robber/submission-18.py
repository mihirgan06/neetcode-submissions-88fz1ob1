class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            given an array nums, nums[i] = the amount of money the ith house has

            houses are arranged in a straight line
            ith house is the neighbor of the i - 1th house and i + 1th house

            you are planning to rob money from the houses but you cannot rob two adjacent houses
            dp[i] the max amount of money you can steal up to and including house i

            nums = [1,1,3,3]
            rob at house 1 then rob house 2

            so 1 + 3 = 4

            nums = [2,9,8,3,6]

            rob at house 1
            then rob at house 3
            total = 12


            option 2:
            rob house 0 then rob at house 1 then 4

            2 + 8 + 6 = 16 --> max

            at each house we need to make the decision to take it or leave it and use our running sum



        '''
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        dp = [0] * n #n + 1 because up to and including the last house

        dp[0] = nums[0] #the max amount of money you can steal at house 0 is nums[0]

        dp[1] = max(nums[0], nums[1])


        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return dp[n - 1]


        