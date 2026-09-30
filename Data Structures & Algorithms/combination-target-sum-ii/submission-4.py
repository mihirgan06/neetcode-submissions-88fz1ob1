class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
            given list of integers candidates
            which may contain duplicates and a target integer target

            we want to return a list of all unique combinations of candidates where the chosen numbers sum to target
            each element must be chosen at most once within a combinations

            we cant use duplicates essentially

            so we need an additonal check if nums[i-1] == nums[i]
            
        '''
        candidates.sort()

        res = []
        path = []


        def dfs(start, total):
            #if we hit the target thats when we return after appending


            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()
        dfs(0, 0)
        return res

            

            


            



