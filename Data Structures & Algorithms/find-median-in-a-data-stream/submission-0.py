import heapq
class MedianFinder:
    '''
        Median = middle value in a sorted list of integers
        if list is even length, there is no middle value, so the median is the mean of the two middle values

        [1,2,3] --> median = 2
        [1,2] --> median = (1 + 2) / 2 = 1.5
        Input:
        ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

        create a new array
        add 1 to the array
        find median of 1 and null 1

        create a small heap, and large heap

        Large is a min heap
        small is a max heap
        
        For insert, we check if the value < smallest value from large




    '''

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            #if the number is larger than the min value in the large heap
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num) #multiply by -1 for max heap

        #rn we unconditionally push to small for the size so now we check the size

        if len(self.small) > len(self.large) + 1:
            new_val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, new_val)
        if len(self.large) > len(self.small) + 1:
            new_val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * new_val)
        


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            median = (-self.small[0] + self.large[0]) / 2.0
            return median
        elif len(self.small) - len(self.large) == 1:
            #small is greater by 1 so the median is the max from small
            return -1 * self.small[0]
        
        elif len(self.large) - len(self.small) == 1:
            return self.large[0]

        
        
        