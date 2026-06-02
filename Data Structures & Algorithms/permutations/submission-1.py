class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            For permiutations we return all possible permutations unlike subsets
            we include all possible permutations all the different ways we can reorder an array

            say [1,2,3] this can be reordered as
            - [1,2,3]
            - [1,3,2]
            - [2,1,3]
            - [2,3,1]
            - [3,1,2]
            - [3,2,1]
        '''
        res = []
        permutations = []
        used = set()

        def backtrack():
            #base case append a full slice
            if len(permutations) == len(nums):

                res.append(permutations[:])
                return
            for num in nums:
                if num in used:
                    continue
                permutations.append(num)
                used.add(num)
                backtrack()
                permutations.pop()
                used.remove(num)
        backtrack()
        return res


            
                
            
            



            
        backtrack(0)
        return res




        