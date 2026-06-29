import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            kth largest element in the array: kth largest elemnt in sorted order


            [2,3,1,5,4], k = 2
            return 4 --> second smallest element 

            we want to account for duplicates
            [2,3,1,1,5,5,4], k = 3
            sort the array -->
            [1,1,2,3,4,5,5], k = 3
            the 3rd largest element here is 4 so return that


            if we can heapify so there's only k elements returning the root is the kth largest element

            Heapify nums so we have a min heap

        '''
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
            #pop from nums while its larger than k
        #after this while loop terminates we should only have k elements

        return nums[0]


        