import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            Given a 2D array points, points[i] = [xi, yi]
            also given an integer k, return the k closest points to origin

            Compiute the distance with the origin
            Create a heap with the heap with the distance return the k smallest from popping k times
        
        '''
        heap = []
        res = []
        for x, y in points:
            dist = math.pow((math.pow(x - x, 2) + math.pow(y - y, 2)), 1/2)
            heap.append([dist, x, y])
        heapq.heapify(heap)

        for i in range(0, k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
        

        
        
            