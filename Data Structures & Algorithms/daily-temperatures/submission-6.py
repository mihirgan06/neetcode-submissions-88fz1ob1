class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Given: array of integers temperatures
            temperatures[i] = daily temperature on the ith day

            Result --> result[i] = number of days after the ith day before a warmer temp appears on a future day

            Initialize result to all 0s size of temperatures
            we can hold a stack where the top of the stack is the index for the highest temp weve seen so far
            while iterating through temperatures if we see a warmer day pop from the stack
            append the differences in indices to res

        '''
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res

        