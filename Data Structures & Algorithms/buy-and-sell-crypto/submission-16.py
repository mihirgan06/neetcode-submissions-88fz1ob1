class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Given: integer array prices
            prices[i] is the price of neetcoin on the ith day
            choose a singke day to buy one neetcoin and choose a diff day in the future to sell it
            return the max profit


            prices = [10,1,5,6,7,1]

            start l at 0
            if prices[r] > prices[l] compute the profit
            and then slide l to the right
        '''
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
        return max_profit