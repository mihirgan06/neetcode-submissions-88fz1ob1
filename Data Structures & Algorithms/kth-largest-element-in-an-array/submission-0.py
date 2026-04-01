class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #given unsorted array of integers and an integer k, return the kth largest element in an array

        #by kth largest elemnt we mean the kthe largest element in sorted order, not the kth distinct element


        #if we push it into a min heap we can do same alg as before

        #if we only care about the k largest, i have to keep track of k numbers specficalky k largest nubers
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        