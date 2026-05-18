class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            piles = array of number of bananas 
            h = number of hours to eat ALL bananas
            k = bananas/hour eating rate
            Each hour choose a pile of bananas and eats k bananas from the pile, 
                If pile has <k bananas, you may finish eating from the pile CANNOT move piles
            return the min k such that you can eat all the bannas within h hours
            h is always greater than piles.length (number of piles)
            THE WORSE CASE is that k = the biggest in the list, this is the case if h = the number of piles

            Goal O(nlogm), O(1) we cannot creatge any new arrays or anything

            
        '''
        #lower bound of k = 1 (BEST CASE)
        #upper bound if h == len(piles), we knopw k must equal the largest pile in piles
        #values of krange from [1 to the max(piles)]

        l = 1 #lower bound ==> k = 1
        r = max(piles) #max value of k which is max(piles)
        #we need to find a value between these two bounds
        while l <= r:
            k = (l + r) // 2 #round down integer division
            hours = 0
            for p in piles:
                #try each pile
                hours += math.ceil(p / k)
            if hours <= h:
                #find smaller rate
                res = min(res, k)
                r = k - 1
            else:
                #too small find bigger rate
                l = k + 1


        return res



            
        