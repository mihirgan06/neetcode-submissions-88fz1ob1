class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        '''
            given an arraya of positive integers nums

            return true if you can partition into two equal subsets
            else return false
            nums = [1,2,3,4]

            true --> 1 + 2 + 3 + 4 = 10 so its possible to get to two arrays of sum 5

            [1,4] and [2,3]


            nums = [1,2,3,4,5]
            1 + 2 + 3 + 4 + 5 = 15 not possible to get to a sum of 7.5

            False if sum(num) is odd







        '''
        target = sum(nums) // 2
        #our goal is to make a subset of nums with sum == target
        dp = [False] * (target + 1)
        #base case = true, we cna make an array = 0
        dp[0] = True
        if sum(nums) % 2 == 1:
            return False
        for num in nums:
            for s in range(target, num -1, -1):
                dp[s] = dp[s] or dp[s - num]
        return dp[target]






