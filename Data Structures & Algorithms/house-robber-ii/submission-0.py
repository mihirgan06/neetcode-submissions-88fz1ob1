class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Same as House Robber 1, but the houses are arranged in a circle rather than a straight line


            nums = [3,4,3]

            3   -  3

            \ 4  /
            Cant hit the last and first one
            Option 1: rob houses from 0 to n-2
            Exclude the last house.

            Option 2: rob houses from 1 to n-1
            Exclude the first house.
            
        '''
        if len(nums) == 1:
                return nums[0]
        def helper(nums):

            cache = [-1] * len(nums)

            def dfs(i):
                
                
                if i >= len(nums):
                    #we went past the hosues

                    return 0
                if cache[i] != -1:
                    return cache[i]
                include = nums[i] + dfs(i + 2)
                disclude = dfs(i + 1)

                cache[i] = max(include, disclude)
                return cache[i]
            return dfs(0)
        return max(helper(nums[:-1]), helper(nums[1:]))




