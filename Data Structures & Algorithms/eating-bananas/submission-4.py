class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            given an integer array piles, piles[i] = numgber of bananas in the ith piles

            you are also given an integer h which represents the number of hours you have to eat all the bananas
            you decide your bananas/hr = k
            --> each hours you may choose a pile of bananas and eat k bananas from that pile
            if the pile has less than k bananas you may finish eating the pile but may not eat from other pile in same hours

            return min integer k such that you can eat all the bananas within h hours

            piles = [1,4,3,2], h = 9

            k = 2

            hour 1 eat 1 bananas
            hour 2 eat 2 from index 1
            hour 3 eat 2 from index 1

            hour 4 eat 2 from index 2
            hour 5 eat 1 from index 2
            hour 6 eat 2 from index 3

            piles = [25,10,23,4], h = 4

            size of array is 4, so we need to finish at least 25 in one hour to move to next pile

            h >= len(piles)
            upper bound is the length of the piles
            if h == len(piles) --> k = max piles
            we can start with k = max(piles) and try to find a better soltuion from there



        '''
        
        l = 1
        r = max(piles)
        res = r #max piles will always work so start it here
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            
            
        


        




        