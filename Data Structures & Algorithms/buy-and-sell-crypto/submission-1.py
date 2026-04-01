class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i, price in enumerate(prices[1:]):
            profit = price - min_price
            max_profit = max(max_profit, profit)
            if price < min_price:
                min_price = price
        return max_profit

            


            