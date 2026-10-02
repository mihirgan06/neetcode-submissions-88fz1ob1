import heapq
class MedianFinder:
    '''
        median = middle valye in sorted lsit of integers


        for lists of even length there is no middle value. sp the median is the mean of two middle values


        2 heaps
        min heap for the large values
        max heapf or the small values

        ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
        [null, null, 1.0, null, 2.0, null, 2.0]



    '''

    def __init__(self):
        self.small = []
        self.large = []

        

    def addNum(self, num: int) -> None:
        '''
            we have to add a number to the right heap
            if the num > the smallest value in the max heap for large then append to larg heap
            then we needc to pop to make the difference between sizes of the heap at most one
        '''
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        while len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        while len(self.small) - len(self.large) > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) - len(self.large) == 1:
            return -self.small[0]
        else:
            return self.large[0]

        
        
        