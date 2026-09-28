class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
            you are given 2d array points
            points[i] = [xi, yi]
            represents the coordinates of a point on xy axis plane
            you are also given an integer kClosest
            return the k closest points to the origin


            distance formula = sqrt((x1 - x2)^2 + (y1 - y2)^ 2)

            points = [[0,2],[2,2]], k = 1


            append till the heap is size of k


        '''
        heap = []
        res = []
        for x, y in points:
            distance = math.pow(math.pow((x - 0),2) + math.pow((y - 0), 2), 0.5)
            heap.append((distance, x, y))
            #append a tuple of distance, x, y
        

        heapq.heapify(heap)
        #when we heapify this its heapified based on distance

        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res



        
            


        