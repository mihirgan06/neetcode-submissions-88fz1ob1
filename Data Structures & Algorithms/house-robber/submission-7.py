class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given:
                Nums, nums[i] = amount of money the ith house has
                houses in a straight line, ith is the neighbor of i -1 and i + 1
                Cannot rob two adjacent houses
                Return max amount of money you can rob

            nums = [1,1,3,3]
            1 and 3

            nums = [2,9,8,3,6]
            2,8,6
        '''
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            #if we go past the last house return 0
            if i >= n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return cache[i]
        return dfs(0)
            

            


        