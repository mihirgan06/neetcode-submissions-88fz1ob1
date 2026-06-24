import heapq
class KthLargest:
    '''
        design a class to find the kth largest integer in a stream of values including duplicates

        EX: 2nd largest from [1,2,3,3] = 3

    '''

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        #maxheap the function
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

        



        
