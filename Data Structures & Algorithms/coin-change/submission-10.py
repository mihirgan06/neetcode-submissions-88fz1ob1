class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            given an integer array coins with diff denominations and an integer amount representing a target amount
            return the fewest amount of coins that you need to make up the exact target else return - 1

            coins = [1,5,10], amount = 12
            3 to make 12
            use 1 10 and 2 1s

            coins = [2], amount = 3

            not possible

            dp[i] = fewest amount of coins needed to make amount i







            
        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 #you need 0 coins to amke an amount of 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
