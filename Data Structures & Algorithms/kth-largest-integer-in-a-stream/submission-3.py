import heapq

class KthLargest:
    '''
        Goal is to keep only the k elements in so we can just take the first index and thats the kth largest for a min heap
    '''

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        #push the value into the heap into its right place (o(logn))
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        
