class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            given an array of positive integers nums

            return true --> partition into 2 subsets subset 1 and subset2 where sum == sum subset2
            return false otherwise


            [1,2,3,4]
            [1,4] [2,3]

            [1,2,3,4,5]
            no possible partition

            can we have dp be a boolean array?
            intialized to all None at first


            dp[i] would mean true or false for a valid partition at that point in the array
            if the total is odd --> impossible (BASE CASE)
            our target is the total // 2

            ex: [1,2,3,4]
            total = 10
            target = 5
            create an array of size 6
            [0,1,2,3,4,5]






        '''
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False] * (target + 1)

        dp[0] = True
        #not possible to make a parition for a array of size 1
        for num in nums:
            for s in range(target, num - 1, - 1):
                dp[s] = dp[s] or dp[s - num]
        return dp[target]




        