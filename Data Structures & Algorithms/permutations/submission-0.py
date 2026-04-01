class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #given array nums of unique integers, return all the possible permutations

        #ok to make these permutations: 

        '''
        for each number in nums, we must explore each possible following numnber
        1 -> 2 -> 3, 1 -> 3 -> 2 (all possible permutations starting with 1)
        2 -> 1 -> 3, 2 -> 3, 1 (all possible permutations starting with 2)
        3 -> 1 -> 2, 3 -> 2 -> 1 (all possible permutations starting at 3)


        we need to iterate through the array and explore the possible next options
        '''
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(i, path, used):
            if len(path) == n:

                res.append(path[:])

                return
            
            for i in range(n):
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(i, path, used)
                path.pop()
                used[i] = False

        
        backtrack(0, [], used)
        return res
                    





            

        