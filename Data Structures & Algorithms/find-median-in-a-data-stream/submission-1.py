import heapq
class MedianFinder:
    '''
        median is the middle value in a sorted list of integers

        for lists of even length, there is no middle value so the median is the mean of two middle vlaues

        [1,2,3] --> median - 2
        [1,2] --> median = 1.5

        we want findmedian to be O(1)
        we can access top of a heap in O(1)


        small values --> maxheap
        large values --> min heap


        [1,2,3,4,5,6

        lower half = [1,2,3]
        upper half = [4,5,6]

        since its even median for even count is (3 + 4) / 2

        odd number:
        1,2,3,4,5

        lower half = [1,2,3]
        upper half = [4,5]

        extra element is in one of the two heaps so 3




    '''

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        #decide which half the value belongs to
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        #size constraint, becasue we are just pushign numbers into the two heaps one hjeap could become considerably larger than the other


        #what if small has too many elements
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        #what if large has too many
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, - val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return  - self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


        
        