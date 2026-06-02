class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
            similar to combination sum but we cannot use the same integer multiple times

            with backtracking create a result and subset array
            Iteration approach --> iterate througj and recurse on i +1 so we dont use the same int
        '''
        candidates.sort()
        res = []
        combination_sum = []
        def backtrack(path, total):
            if total == target:
                #if we hit the target then return
                #append copy of the subset array to result
                res.append(combination_sum[:])
                return
            if total > target:
                return
            for i in range(path, len(candidates)):
                if i > path and candidates[i] == candidates[i - 1]:
                    continue
                combination_sum.append(candidates[i]) #append a candidate
                total += candidates[i] #append the value to the total
                backtrack(i + 1, total)
                #start backtracking ont he next value
                combination_sum.pop()
                #pop and try without
                total -= candidates[i]
        backtrack(0, 0)
        return res





        
        