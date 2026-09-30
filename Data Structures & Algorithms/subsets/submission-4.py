class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            nums = [1,2,3]
            [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

            2^n subsets
            3 elements so 8 subsets
            take/leave at every step




            [1,2,3]

            []      [1]

        []      [2].        [1] [1,2]
       [] [3]. [2][2,3] [1] [1,3]. [1,2] [1,2,3]
       leaves are all the subsets

       dfs(i, current_subset)

       we can either skip nums[i]
       or we can take nums[i]

       subset.append(nums[i])
       dfs(i + 1)
       subset.pop()

        
        '''
        res = []
        subset = []

        def dfs(i):
            #base case once youve made a skip/take decision for every number, youve created one complete subset
            if i >= len(nums):
                res.append(subset.copy())
                return 
            #take decision
            subset.append(nums[i])
            dfs(i + 1)

            #skip decision
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res