class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        given an array of nums of unique integers
        nums = [1,2,3]
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        return all possible permutations each level should try every possible uniqeu permutations
        we can use a set to check if weve used an element alr for the permutation generated at the level


        '''
        res = []
        path = []
        used = set()


        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                dfs()
                used.remove(num)
                path.pop()
        dfs()
        return res

            