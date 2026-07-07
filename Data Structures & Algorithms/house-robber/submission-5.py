class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given array nums, nums[i] = amt of money the ith house
            Houses are arranged in a straight line
            ith house is neighbors with i-1 and i + 1 house

            cannot rob 2 adjacent houses
            nums = [1,1,3,3]
            max amt of money = 4 either nums[0] and nums[2] or nums[1] and nums[3]
            either way this doesnt overwrite our current max

            nums = [2,9,8,3,6]

            max amt of money = options = 16 or 12 so we can steal 16
            Base cases:
            - if we go apst the last house return 0


        '''
        cache = [-1] * len(nums)
        #array of -1 for cache of size n

        def dfs(i):
            if i >= len(nums):
                return 0
            
                
            if cache[i] != -1:
                return cache[i]

            rob_current = nums[i] + dfs(i + 2)
            rob_next = dfs(i + 1)
            
            cache[i] = max(rob_current, rob_next)
            return cache[i]
        return dfs(0)
              