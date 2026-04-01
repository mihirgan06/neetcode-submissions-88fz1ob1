class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = [] #what we add the subsets to

        def backtrack(i, subset):
            if i == n: #we want to hit the case of being at a leaf
                res.append(subset[:])
                #make a COPT so we dont overwrite it
                return
            #all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset) 
            #takes care of all subsets that include this number
            subset.pop()


            #all subsets that do NOT include nums i
            while i + 1 < n and nums[i] == nums[i + 1]:
                #as long as the next index is in bounds AND the next index is a duplicate value
                #we should add it to the array

                i += 1
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return res
                

            
            
            
            

            


            

        
        