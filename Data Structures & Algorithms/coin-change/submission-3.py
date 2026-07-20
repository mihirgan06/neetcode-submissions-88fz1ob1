class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Given an integer array coins
                - coins of diff denominations 
                [1,5,10] amount = 12
                return the fewest number of coins to get to targetr

                answer = 3 2(1) + 10
                [2]. amount = 3
                -1 --> impossible

                [1], amount = 0
                0 you can choose 0
        '''
        cache = [-2] * (amount + 1)

        def dfs(remaining):
            #if we try a coin we need to subtract that from our remaining
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            if cache[remaining] != -2:
                return cache[remaining]
                
            num_coins = math.pow(2, 31) -1

            for coin in coins:
                result = dfs(remaining - coin)
                #recurse on the remaining after using one of the coins
                if result != -1:
                    num_coins = min(num_coins, result + 1)
            cache[remaining] = num_coins if num_coins != math.pow(2, 31) - 1 else -1
            return cache[remaining]
        final_res = dfs(amount)
        return final_res

        