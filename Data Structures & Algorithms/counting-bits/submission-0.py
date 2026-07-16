class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
            Given an integer n, count the numnber of 1s in the binary rep of every number in the range [0,n]

            return an array output where output[i] is the number of 1s
            inialize res as all 0s



        '''
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i&1)
        return dp

