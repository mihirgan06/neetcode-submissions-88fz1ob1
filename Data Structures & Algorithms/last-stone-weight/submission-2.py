import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Given an array of integers stones, where stones[i] represents the weight of the ith stone
            At each step, choose the two heaviest stones, with weight x and weight y
            smash the two stones together
            if x == y then both are destroyed
            if x < y we push the new weight of y - x

            Convert into a max heap

        '''
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            # - to convert back into positive number
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x == y:
                heapq.heappush(stones, 0)
            elif x > y:
                heapq.heappush(stones, -(x - y))
            elif y > x:
                heapq.heappush(stones, -(y - x))
        return - stones[0]
            
        