class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            given: 2d array points, points[i] = [xi, yi]
            represents the coordinates of a point on an X-Y axis plane
            also given k 
            return the k closest points to the origin
            points = [[0,2],[2,2]], k = 1
            we can use a minheap based on distance and pop k elements and append to a res array
        '''
        res = []
        heap = []

        for x, y in points:
            distance = math.pow(math.pow(x - 0, 2) + math.pow(y - 0, 2), 0.5)
            heap.append((distance, x, y))
        heapq.heapify(heap)
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
         

        