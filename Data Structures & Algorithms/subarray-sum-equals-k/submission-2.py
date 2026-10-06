class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            Given: array of integers nums, and an integer k

            return: total number of subarrays whose sum == k
            nums = [2,-1,1,2], k = 2
            [2]
            [2, -1, 1]
            [-1,1,2]
            [2]

            prefix sum + hashmap
            at eahc number we need to know what is needed to get to target and see if that is possible to create
            


        '''
        prefix_counts = defaultdict(int)

        prefix_counts[0] = 1
        res = 0
        curr_sum = 0

        for i in range(len(nums)):
            
            curr_sum += nums[i]
            if curr_sum - k in prefix_counts:
                res += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1
        return res
        