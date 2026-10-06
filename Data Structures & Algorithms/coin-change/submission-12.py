class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Given:
                integer array coins of differnet denominsations 
                and integer amount == target amount

            return:
                fewest amount of coins that you need to make up the exact target amount
                if it is impossible to make the amount return -1

            coins = [1,5,10], amount = 12
            12 = 10 + 1 + 1
            3 coins


            coins = [2], amount = 3

            amount of 3 cannot be made with coins of 2

            return -1

            coins = [1], amount = 0
            0 choosing 0 coins is valid
            dp array of size amount
            dp[i] = fewest amount of coins needed to make amount of i


            

        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 #amount of 0 we can make in 0 ways


        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                


        