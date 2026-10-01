class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            givena n integer array coins representing cons at diff denominations
            integer amount representing a target amlunt of money
            return the fewest number of coins that you need ot make up exact target

            if impossible to make up the amount return -1

            dp[i] = fewest amount of coins needed to make an amount of i

            if amount =3
            dp array = [0, 1, 2, 3]

            dp[n] = fewest amt of coins to make amount of n

        '''
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        #0 coins to make an amount of 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]





        