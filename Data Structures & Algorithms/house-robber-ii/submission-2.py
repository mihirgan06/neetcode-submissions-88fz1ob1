class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given:
                nums, nums[i] = amount of money the ith house has
                Houses arranged in circle, first and last houses are neighbors
                cannot rob 2 adjacent houses
            
            Top Down Approach:
                Cache array
                if i goes past len(nums) we wanna return 0




        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(nums):
            local_n = len(nums)
            cache = [-1] * local_n
            def dfs(i):
                if i >= local_n:
                    return 0
                
                if cache[i] != -1:
                    return cache[i]
                
                cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
                return cache[i]
            return dfs(0)
        return max(helper(nums[0:-1]), helper(nums[1:]))
