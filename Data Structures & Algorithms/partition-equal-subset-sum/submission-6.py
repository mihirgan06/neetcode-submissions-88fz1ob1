class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            given an array of positive integers nums

            return true if you can parittion the array into two subsets
            sum(subset1) == sum (subset2) --> True else false


            nums = [1,2,3,4]
            1 + 4 = 5
            2 + 3 = 5
            Approach:
            1. if the sum of nums is odd its not possible to make two equal subsets
            2. create a dp array of boolean type
            3. the array should be the size of target + 1 where target is half of the total
            4. if one subset can equal target, it means the other must equal the other half of the target
            5. dp[i] whetehr it is possible to create a subset of target i
        '''
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for s in range(target, num -1, -1):
                dp[s] = dp[s] or dp[s - num]
        return dp[target]
        
        