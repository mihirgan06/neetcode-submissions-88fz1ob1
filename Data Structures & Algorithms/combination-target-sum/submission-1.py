class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        '''
            Similar to subsets where we need to backtrack and do a complete search
            The difference is our stoping base case would be if the values of our 
            combo sum = the target
        '''

        combination_sum = []
        res = []
        def backtrack(path, total):
            if total == target:
                res.append(combination_sum[:])
                return
            if total > target:
                return
            

            for i in range(path, len(nums)):
                #loop versoin include, backtrack, exclude
                combination_sum.append(nums[i])
                total += nums[i]
                backtrack(i, total)
                combination_sum.pop()
                total -= nums[i]

        backtrack(0, 0)
        return res

        