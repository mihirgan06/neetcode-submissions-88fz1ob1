class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
        We want to find the number of days at EACH temperature befor ethe next warmer temperature 
        O(N) time complexity

        Approach:
        We can iterate through the array 
        Push to stack
        Monotonic decreasing stack



        '''
        res = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            #print(temperature)
            #push each temperature into the stack
            
            while stack and temperature > temperatures[stack[-1]]:
                if temperatures[i] > temperatures[stack[-1]]:
                    prev = stack.pop()
                    res[prev] = (i - prev)
            stack.append(i)
        return res




        