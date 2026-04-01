class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given an integer array nuns, and integer k --> return the k most frequent elements within the array
        #if we were to use a min heap, we can convert the array to a min heap
        #map to count the frequency of the elements in the array
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        #we have now a num: frequency pairing inside map
        # To use a min-heap for top K, we store (frequency, num) so heapq sorts by frequency
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the numbers from the (count, num) tuples
        return [item[1] for item in heap]