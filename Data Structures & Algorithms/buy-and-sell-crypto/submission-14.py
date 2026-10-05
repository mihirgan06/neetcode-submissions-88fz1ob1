class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            given:
            prices = prices[i] is the price on the ith day
            you may choose a single day to buy one coin and choose a diff day in future to sell
            we onjly want to sell if its profitable
            sliding window variable
            start l and r at 0
            if profitable as in nums[r] - nums[l] add to profit return max profit

        '''
        l = 0
        max_profit = 0
        profit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r

                
                
            max_profit = max(max_profit, profit)
        return max_profit



        