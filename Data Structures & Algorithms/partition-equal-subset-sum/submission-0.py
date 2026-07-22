class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            Given an array of nums
            return true if you can partition into 2 subsets, subset1 and subset2 
            where sum(subset1) == sum(subset2)
            else reutrn false


            nums = [1,2,3,4]
            return true


            nums = [1,2,3,4,5]
            return false
            to be a valid partition there must nto be an alement left out
            for ex: [1,2,3] and [5] isn't valid cuz we leave out that there 4


            Define total as the sum of the nums array
            total = 2 * sum(A) a is the first subset, this is always even

        '''
        total = sum(nums)

        if total % 2 != 0:
            return False
        target = total // 2

        n = len(nums)
        cache = [[None] * (target + 1) for i in range(n)]

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            
            if i >= n or curr_sum > target:
                return False
            if cache[i][curr_sum] is not None:
                return cache[i][curr_sum]
            
            take = dfs(i + 1, curr_sum + nums[i])
            skip = dfs(i + 1, curr_sum)
            cache[i][curr_sum] = take or skip
            return cache[i][curr_sum]
        return dfs(0,0)
        


        