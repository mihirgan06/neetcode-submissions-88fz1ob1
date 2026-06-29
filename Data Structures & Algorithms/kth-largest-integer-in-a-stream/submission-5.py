import heapq
class KthLargest:
    '''
        design a class to find the kth largest integer in a steam of values including duplicates

        [1,2,3,3] --> second largest = 3
        stream isnt sorted

        Initialize a heap and have it sort so that there are only k elements in the heap
        the first element of a min heap with k elements is by def always the kth largest leemnt
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        #initialize nums and k as objects we can instantiate and modify
        #convert nums into a min heap
        heapq.heapify(self.nums)
        #while there are more elems in nums than k we want tto pop so theres a max of k elements
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
            #the size of nums decreases everytime we pop which activates the condition

        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return heapq.heappop(self.nums)
        
