import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            Given 2D array points: points[i] = [xi, yi] = coordinates of a point on X-Y axis
            also given an integer k
            Return the k-closest points ot the origin (0, 0)
            distance = (sqrt(x1-x2)^2 + y1-y2)^2

            We can disregard the square root here
            we want the k closest points
            so the 1st clostst point would be the point with the smallest distance

            Min heap, return the k closest points
        '''
        heap = []
        res = []
        #iterate through points and compute distance
        for x, y in points:
            dist = math.pow((x - 0), 2) + math.pow((y - 0), 2)
            heap.append([dist, x, y])
        heapq.heapify(heap)

        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
            

                        