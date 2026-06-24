import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Given an array of integers stones where stones[i] = weight of the ith stone

            At each step we choose the two heaviest stones and smash:
                if x == y:
                    both stones are destroyed
                if x < y:
                    x is destroyed, stone of y has new weight y - x
            stones = [2,3,6,2,4]
            output = 1
            smash 6 and 4 and are left with 2, [2,3,2,2]
            smash 3 and 2 and are left with 1 ==> [1,2,2]
            smash 2 and 2 so array becomes [1]


            use a max heap so that we start by smashign the two largest stones
        '''
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        #create a max heap 
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                heapq.heappush(stones, 0)
            elif x > y:
                heapq.heappush(stones, - (x - y))
            elif y > x:
                heapq.heappush(stones, - (y - x))
            else:
                return 0
        return - stones[0]
        