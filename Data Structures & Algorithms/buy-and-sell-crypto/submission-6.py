class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        ans = 0
        for right in range(length):
            left = 0
            while left < right:
                print(prices[left], prices[right])
                ans = max(prices[right] - prices[left], ans)
                left += 1
        return ans