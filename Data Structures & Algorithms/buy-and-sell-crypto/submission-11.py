class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        ans = 0
        left = 0
        for right in range(1, length):
            if prices[left] > prices[right-1]:
                left = right-1
            ans = max(prices[right] - prices[left], ans)
        return ans