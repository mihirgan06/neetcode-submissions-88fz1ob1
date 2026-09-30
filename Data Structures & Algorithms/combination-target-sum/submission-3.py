class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            given an array of distinct integers nums and a target
            return all list of unique combinations of nums where the chosen numbers sum to target

            the same number may be chosen from nums unlimited times

            two combinarions are the same if the frequency of each of the chosen numbers is the same, otherwise they are differnet

            nums = [2,5,6,9]
            target = 9
            [2,2,5],[9]
            we have to take with a boolean if the current sum = target then pop and recurse again

        '''
        res = []
        path = []
        path_sum = 0
        def dfs(i):
            nonlocal path_sum

            if path_sum == target:
                res.append(path.copy())
                return
            if path_sum > target or i >= len(nums):
                return
            #take
            path.append(nums[i])
            path_sum += nums[i]
            dfs(i) #same i --> reuse this number
        
            #skip
            path.pop()
            path_sum -= nums[i]
            dfs(i + 1)


        dfs(0)
        return res
            
            

