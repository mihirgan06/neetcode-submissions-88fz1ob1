import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            given an unsorted array of integers nums and an integer k
            return the kth largest element in the array

            heap approach: O(n logn)
            heap operations are logn and we perform n of them
            nums = [2,3,1,5,4], k = 2
            we can create a heap and push every elem onto the heap
            pop till we have k elements in the heap then the top is the kth largest element
            min heap guaranteed the smallest element is the top of the heap

        '''
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]
            
        