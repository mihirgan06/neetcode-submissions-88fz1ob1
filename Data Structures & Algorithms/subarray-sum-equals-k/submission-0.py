class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
            given: array of integers nums, and an integer k

            return the total number of subarrays whose sum = k
            nums = [2,-1,1,2], k = 2

            sliding window:
            start l and r at 0
            first sum is 2 shift l
            we shift when our sum == k

            Sliding window doesnt work --> negative sums


            we can use a hashmap
            iterate left to right
            build a prefix sum, see if what we need to make target is in the hashmap

        '''
        prefix_counts = {0 : 1}
        res = 0
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            needed = current_sum - k
            if needed in prefix_counts:
                res += prefix_counts.get(needed)
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        return res


            




        


        