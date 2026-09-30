class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            given an integer array coins of diff denominations and an integer amount representing total amount of money


            return the fewest number of coins that you need to make up the exact target amount
            dp[i] = min number of coins that you need to make the exact target amount
            if impossible return -1
            initlaize a dp array of size amount


        '''
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    #min of current dp[i] and dp[i - coin] and an additional coin
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
        
                    
            
        