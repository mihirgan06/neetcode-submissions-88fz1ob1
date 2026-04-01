class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #given 2D array points, where points[i] = [xi, yi] represents coordinates of X,Y plane
        #also givne an integer k
        #return k closest points to the orign
        #distance btween two points = (sqrt((x1-x2)^2 + (y1-y2)^2))

        #we can kinda do a similar approach to kthfrequest elements in the sense we can use a min heap and push as long as the heap size is less than k
        #however, we want to return result when the distance formula returns the smallest value


        #given points

        heap = []
        #we choose to use an empty heap instead of hrspify,
        #whenever we want only the bst K elements we use an empty heap
        #in situations we want everything in the heap we would use heapify

        #in any top K selection problem --> use an empty heap and push items one by one
        #pop when the size > k
        res = []

        for x, y in points:
            #iterate throught he points array
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(heap, (- dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        for tup in heap:  # tup is (dist, x, y)
            dist, x, y = tup  # Unpack all three
            res.append([x, y])  # Ignore dist

        return res
        