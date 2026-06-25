import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ''' 
            Return the kth largest element in the array
            kth largest element, if we only have k elements in the array this is just the otp element root is the kth largets


        '''
        #turn the array into a minheap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]


        
        