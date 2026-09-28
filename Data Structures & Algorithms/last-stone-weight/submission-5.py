class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            given an array of integers stones,
            stones[i] = weight of ith stones

            at each step we choose the two heaviest stones, with weight x and y and smash them tgt

            if x == y both stones are destroyed
            if x < y stone of wieght x is destroyed and the stone of y has weight y - x

            continue until there is no more thatn one stone remaining
        '''
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)
        #the largest stone
        while len(max_heap) > 1:
            stone_x = - heapq.heappop(max_heap)
            #the second largest stone
            stone_y = - heapq.heappop(max_heap)
            if stone_x == stone_y:
                pass
            elif stone_x > stone_y:
                heapq.heappush(max_heap, - (stone_x - stone_y))
            else:
                heapq.heappush(max_heap, - (stone_y - stone_x))
        return - max_heap[0] if max_heap else 0
