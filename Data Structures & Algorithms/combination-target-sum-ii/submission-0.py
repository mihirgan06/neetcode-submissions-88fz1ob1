class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #thre may be duplicates within the array
        #we cannot use the sam eelemnt multiple times in the same solution array
        res = []
        candidates.sort()
        n = len(candidates)
        #this way we have the items in ascending order


        def backtrack(i, cur, total):
            #we need to skip duplicates
            #we consier the duplicates when deciding the next element after a certain starting position
            #at a given recursion depth, don't start two branches with the same next number

            if total == target:
                res.append(cur[:])
                return
            for j in range(i,n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                
                cur.append(candidates[j])
                backtrack(j + 1, cur, total + candidates[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return res
                
            


            
            


            
