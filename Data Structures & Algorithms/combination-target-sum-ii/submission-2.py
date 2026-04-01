class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
    
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            if total > target or i == len(candidates):
                return
            #include candidates[i]
            cur.append(candidates[i])

            dfs(i + 1, cur, total + candidates[i])

            cur.pop()

            #skip candidates[i]
            #need the whil i + 1 to ensure it doesnt run off the array
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)
    
        dfs(0, [], 0)
        return res