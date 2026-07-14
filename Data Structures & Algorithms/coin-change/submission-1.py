class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Bottom up approach
            create dp array where inf is the base value, a value pf inf mean s igs not possible to return the values
        '''
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        for current in range(1, amount + 1):
            for coin in coins:
                if current - coin >= 0:
                    dp[current] = min(dp[current], 1 + dp[current - coin])
        

        return dp[amount] if dp[amount] != float("inf") else -1