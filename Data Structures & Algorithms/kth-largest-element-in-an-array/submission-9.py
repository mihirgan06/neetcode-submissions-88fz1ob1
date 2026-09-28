class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            given an unsorted array of integers nums and integer k findKthLargest
            by kth largest element we mean the kth largest leement int he sorted order not the kth distinct element
            nums = [2,3,1,5,4], k = 2
            push into a heap

            then return the top of the array
        '''

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]