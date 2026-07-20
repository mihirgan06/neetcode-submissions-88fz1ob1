class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
            COunt the number of 1s in the binary rep for every number inr ange of [0,n]
            make an array of all 0s 
            iterate through appednign the 1s for each slot of dp array and return
        '''
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i&1)
        return dp
            

        