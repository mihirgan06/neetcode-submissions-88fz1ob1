class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
            Given a list return a result list with all the possible permutations of that given list
            The main rule is that each number in nums for ex can only be used once
            So if we have [1,2,3] the valid permutations only use 1, 2, 3 once each in any given order
            '''
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                backtrack()
                used.remove(num)
                path.pop()
                
        backtrack()
        return res

        