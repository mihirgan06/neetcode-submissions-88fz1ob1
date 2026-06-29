import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Given array of integers stones, stones[i] = weight of the ith stone
            At each step choose the two heaviest stones with weight x and weight y
            if we have a max heap than the tow heaviest stones are the twos tones we polp

            If x == y then we get 0
            if x < y then stone x is destroyed and stone y = y - x

        '''
        stones = [- stone for stone in stones]
        heapq.heapify(stones)
        #convert stones into a max heap
        #now the top element of stones is the largest element
        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x == y:
                heapq.heappush(stones, 0)
            elif x < y:
                heapq.heappush(stones, -(y - x))
            elif y < x:
                heapq.heappush(stones, -(x - y))
        if len(stones) == 0:
            return 0
        return - stones[0]
        
        

            


        