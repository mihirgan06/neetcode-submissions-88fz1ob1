class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            given integer array prices, where prices[i] = price at ith day

            Choose a single day to buy one coin and choose a diff day in the future to sell ith

            return max profit you cna receive

            prices = [10,1,5,6,7,1]
            buy at day 1 sell at day 4 make 6 profit

            prices = [10,8,7,5,2]

            no day in the future to sell since its descending

            
        '''
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            profit = prices[r] - prices[l]

            max_profit = max(profit, max_profit)
        return max_profit


            

        