class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            Number of subsets = 2^len(nums)

            helper backtrack function, path
            at each num in nums we have a choice to either include or not include it


        '''
        res = []
        subset = []
        def backtrack(start):
            res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
                
        backtrack(0)
        return res
            

        