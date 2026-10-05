class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            given:
            - integer array piles, piles[i] = number of bananas in the ith pile
            - integer h --> the number of hours you have to eat all the bananas

            Return:
            - bannas per hour eating rate of k
            each hour you may choose a pile of bananas and eat k bananas from that pile
            - if the pile has less than k banans you may finishe ating that pile but cannpot eat from another pile


            Examples:
            piles = [1,4,3,2], h = 9
            the most k can be is the max(piles)
            if k = 4
            we can finish all 4 piles in 4 hours

            we want to binary search on the values of k
            the least we could do is 1 so ebtween 1 and max(piles) we binary search
        '''

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                #total amount of hours to finish all the piles

                hours += math.ceil(pile/k)
            if hours <= h:
                #we found a valid solution but could maube do better?
                res = min(res, k)
                r = k - 1
            #we arent good enough increase k
            else:
                l = k + 1
        return res
                
                
            


        