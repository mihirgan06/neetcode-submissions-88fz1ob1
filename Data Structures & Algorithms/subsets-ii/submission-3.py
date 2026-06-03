class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            given an arrya nums of integers with duplicates
            Return all subsets without duplicate subsets
            Each subset must be unique

            [1,2,1] --> [1,1,2]
            we have to handle duplicates within recursive case if nums[i - 1] == nums[i] we backtrack on i + 1


        """
        nums.sort() #must sort so that we have identical duplicates side by side
        res = []
        subset = []
        def backtrack(path):
            res.append(subset[:])
            for i in range(path, len(nums)):
                #start at path when path = 0
                if i > path and nums[i] == nums[i -1]:
                    #we need the first clause becasuse when path == i we unconditionally append to subset, but when we get further and see duplicates we want to skip and backtrack on i + 1
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return res
            

        