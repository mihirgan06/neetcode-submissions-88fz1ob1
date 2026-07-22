class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [[False] * (target + 1) for i in range(n + 1)]

        for i in range(n + 1):
            #we can a;lways create sum 0 by selecting 0 numbers
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for curr_sum in range(1, target + 1):
                skip = dp[i - 1][curr_sum]
                take = False
                if curr_sum >= nums[i-1]:
                    take = dp[i - 1][curr_sum - nums[i-1]]
                dp[i][curr_sum] = take or skip
        return dp[n][target]

        