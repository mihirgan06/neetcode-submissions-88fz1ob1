class KthLargest:
    import heapq
    #given nukber k, initial list of numbers
    #numbers arrive one at a time
    #after each insertion, we need to find which is the kth largest number thus far

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

        

    def add(self, val: int) -> int:
        #adds the integer val to the stream and returns kth largest #convert array nums into a min heap
        #smallest elements at the top
        #retreiving the smallest element ==> O(1) time and is just nums[0]
        #largest elements would be on the end
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        


        
