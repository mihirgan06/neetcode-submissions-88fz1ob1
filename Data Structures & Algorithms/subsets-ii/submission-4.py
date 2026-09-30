class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
            given duplicates in the subset array
            we need to create all the duplicates possible
            we cant append duplicate subsets so at each level within our loop we need a duplicate check
            first we sort the nums array

        '''
        nums.sort()
        #have duplicates side by side
        subset = []
        res = []

        def dfs(path):
            res.append(subset.copy())

            for i in range(path, len(nums)):
                if i > path and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                dfs(i + 1)
                
                subset.pop()
        dfs(0)
        return res



                

                