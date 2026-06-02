class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
            Sort the nums array to have duplicates next to each other
            We backtrack and try each subset but ignore duplicates
        '''
        nums.sort()
        res = []
        subset = []
        def backtrack(path):
            res.append(subset[:])
            for i in range(path, len(nums)):
                if i > path and nums[i] == nums[i -1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return res
        