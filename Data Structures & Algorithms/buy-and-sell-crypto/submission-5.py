class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' given an integer array prices where prices[i] is the price of NeetCoin on the ith day

            you may choose a single day to buy a neetcoin and choose a diff day in the future to sell it


            Choose a single day to buy one coin and choose diff day in future to sell it


            max profit you can achieve

            sliding window ==> buy at the lowest price and then sell future at a high price

        '''
        l = 0
        max_profit = 0


        for r in range(len(prices)):
            if prices[r] >= prices[l]:
                #profitable
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            
            while prices[r] < prices[l]:
                #not profitable at all
                l += 1
                #move left forward
        return max_profit



        