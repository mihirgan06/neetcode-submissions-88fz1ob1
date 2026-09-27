class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            you are givne an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith daily
            return an array result where result[i] is the number of days after the ith day before a warmer temperature appears ona. future day

            temperatures = [30,38,30,36,35,40,28]
            [1,4,1,2,1,0,0]

            temperatures = [22, 21, 20]
            [0,0,0]
            if temperatures are decreasing then obv there would be no warmer temperatures so 0s across the board

            Iterate through temperatures
            keep an additional stack array 
            for each temperature there is acorresponding value in the new stack we made letting us hold the number of days till a higher temp is seen






        '''
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res