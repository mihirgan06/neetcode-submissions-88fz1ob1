class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Given an integer array nums

            nums[i] = the amount of money the ith house has
            houses are arranged in a straight line

            If i want to rob the houses
            I cannot rob two adjacent houses

            1) Top Down approach

                Cache array
                I can'y go to two adjacent house so i can only hit houses i -1 and i + 1


                [1,1,3,3]
                1, 3 ==> 4

                [2,9, 8,3,6]
                16
            
            the cache array should be the len(nums) 
        '''

        
        n = len(nums)
        cache = [-1] * n
        

        def dfs(i):
            n = len(nums)
            if i >= n:
                #weve gone past the last house
                return 0
            if cache[i] != -1:
                return cache[i]
            
            #cache[i] = the money we could get at house i plus the money we could get recursively at house - 1 and house + 1
            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)
        
            return max(rob_current, skip_current)
        #start at first index
        return dfs(0)

        


