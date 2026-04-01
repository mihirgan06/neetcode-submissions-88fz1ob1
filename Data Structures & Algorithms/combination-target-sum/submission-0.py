class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #we want combinations -- Order and items in the list doesnt matter
        nums.sort()
        res = []
        n = len(nums)
        #cur is going to be a list to represent what weve added to the current combination
        #total maps to the total sum of cur array so we can check if its target
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            #out of bounds check
            if i >= n or total > target:
                return
            
            cur.append(nums[i])

            #decision where we do include the candadite
            backtrack(i, cur, total + nums[i])
            #if we decide NOT to include candadite
            cur.pop()

            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res

            

