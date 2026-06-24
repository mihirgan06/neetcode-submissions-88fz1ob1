import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            Given a 2D array points where poitns[i] = [xi, yi]
            also givne an integer k
            Return the k closest points to the origin

            distance = (x1 - x2)^2 + (y1 - y2)^2
            create a distance heap of points

            points = [[0,2], [2,2]]
        '''
        heap = []
        for x,y in points:
            dist = x*x + y*y

            heap.append([dist, x , y])
        heapq.heapify(heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1

        return res
        