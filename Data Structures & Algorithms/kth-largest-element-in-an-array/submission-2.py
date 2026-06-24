import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            First heap solution:
                - given unsorted array of numns and k return kth largest elemtn in the array

                kth largest element in sorted order

                without sorting

            Create a max heap of size k, and return the kth element, the kth largest will be the first element of a max heap
        '''
        nums = [-num for num in nums]
        #create max heap

        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
        