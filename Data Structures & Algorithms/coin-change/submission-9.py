class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            given an integer array coins
            representing coins of diff denominations, and an integer amount representing target amt of money

            return the fewest number of coins you need to make up the exact target amount
            dp[i] = the min number of coins needed to make the amount i
            if amount = 12

            create an array of size 13 amount of 0 is basically irrelivant
            

        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
