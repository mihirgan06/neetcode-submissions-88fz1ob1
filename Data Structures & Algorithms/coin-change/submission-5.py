class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            given an integer array coins representing coins of diff denomionations

            1$, 5#
            integer amount with target amount
            fewest number of coins that youy need to reach the target
            if impossible return -1

            coins = [1,5,10], amount = 12

            output = 3
            2 1s and 1 10

            coins = [2], amount = 3

            -1 nto possible

            coins = [1], amount = 0


            take the largest denomination first and try to see how much of the target you can make with that
            then move to the next denomination

            dp[i] at i whats the least amount of coins needed to make the target amount i

            
        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 #we can make the value of 0 using 0 coins
        for i in range((amount + 1)):   
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
                    




        