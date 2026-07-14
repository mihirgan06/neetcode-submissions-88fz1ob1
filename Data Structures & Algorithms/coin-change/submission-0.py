class Solution:
    import math
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Given an integer array coins representing coins of different denominations and an amount integer representimng target money
            coins = [1,5,10], amount = 12
            3: 12 = 10 + 1 + 1
            dont have to use very coin available

            coins = [2], amount = 3
            -1 no way to make 3 with 3



            coins = [0], amount = 0
            output = 0

            Top down:
            - cache array of size amount im thinkign
        '''
        cache = [-2] * (amount + 1)

        def dfs(remaining):
            #base case 1: remaining is 0 we return 0 coins == Success
            if remaining == 0:
                return 0
            #base case 2: failure, remaining < 0 so we rturn - 1
            if remaining < 0:
                return -1
            
            if cache[remaining] != -2:
                return cache[remaining]
            
            num_coins = math.pow(2, 31) - 1
            
            for coin in coins:
                result = dfs(remaining - coin)
                if result != -1:
                    num_coins = min(num_coins, result + 1)
            
            cache[remaining] = num_coins if num_coins != math.pow(2, 31) - 1 else -1
            return cache[remaining]
        
        final_res = dfs(amount)
        return final_res