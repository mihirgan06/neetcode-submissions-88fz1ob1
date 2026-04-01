class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Desired Time Complexity O(LogN) --> Binary Search

        #piles = piles of bannas, index is number of bananas per pile
        #k = number of bananas per hour eating rate
        #Each hour you may choose a pile and eat k bananas
        #If a pile has less than k banans, you may finish the pile biut cannot eat from another pile in same hour

        l = 1

        r = max(piles)
        res = r #initialize it to r bc we know the max works

        #h is always larger than the number of elements in the element

        #If the number of piles > h then there would def be at least one leftover pile


        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            #ypical binary search alg
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res