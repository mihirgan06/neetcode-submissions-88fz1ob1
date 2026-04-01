class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-s for s in stones]
        weight = 0
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = -heapq.heappop(stones) #grab the largest stone fromt he heap
            secondlargest = -heapq.heappop(stones) #second largest
            if largest == secondlargest:
                weight = 0
            elif secondlargest < largest:
                weight = largest - secondlargest
                heapq.heappush(stones, -weight)
        if stones:
            return abs(stones[0])
        return 0
        
            

