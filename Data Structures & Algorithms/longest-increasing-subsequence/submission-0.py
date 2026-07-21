class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            Given an array nums, return length of the longest STRICTLY increasing subsequence
            subseqyebce = seqyebce tgat cab ve deruved by deleting some or no elements without changeing the relative order


            nums = [9,1,4,2,3,3,7]

            1,2,3,7 return 4

            nums = [0,3,1,3,2,3]

            0, 1, 2, 3 return 4

            cache array has the longest subsequence up to i point at cache[i]
            res array we can backtrack on

        '''
        n = len(nums)
        cache = [[-1] * (n + 1) for i in range(n)]

        def dfs(i, prev):
            if i >= n:
                #if we go past the end of the array we shoudl just return 0
                return 0
            if cache[i][prev + 1] != -1:
                return cache[i][prev + 1]
            
            skip = dfs(i + 1, prev)
            take = 0
            if prev == -1 or nums[prev] < nums[i]:
                take = 1 + dfs(i + 1, i)
            result = max(take, skip)
            cache[i][prev + 1] = result
            return cache[i][prev + 1]
        return dfs(0, -1)
            

            
            

