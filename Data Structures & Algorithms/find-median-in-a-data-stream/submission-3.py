import heapq
class MedianFinder:
    '''
        median = middle value in a sorted list of integers
        for lsits of even length, there is no mdidle value so the median is the mean of the two middle values

        Approach (2 heaps):
        - use a min heap for large values
        - use a max heap for small values
        the root from the max heap wil be the largest of the small heaps
        the root from the min heap will be the smallest of the large values
        for an odd number of inputs, whichever is longer will be the median
        for an even number of inputs is the mean of the two
        EDGE CASE:
        - how do we control the size
        if the difference in sizes of the heaps > 1 we should pop and push to the other heap till its normalized
    '''

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, - num)
            #we push the negative because thats how max heaps work
        while len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, - val)
        while len(self.small) - len(self.large) > 1:
            val = - heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) - len(self.large) == 1:
            return - self.small[0]
        elif len(self.large) - len(self.small) == 1:
            return self.large[0]
        else:
            avg = (- self.small[0] + self.large[0]) / 2
            return avg

        
        