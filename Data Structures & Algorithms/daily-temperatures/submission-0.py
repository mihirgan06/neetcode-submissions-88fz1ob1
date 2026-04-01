class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force is a nested loop approach
        result = [0] * len(temperatures) #prefixed size to be the size of the temperatures array but all filled iwth 0s
        stack = [] #to hold indices
        #indices represent number of days between current temperature and the immediate warmer temperature


        for i, val in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #once we find a temperature higher we can pop the old temperature
                #Stack will be in decreasing or equal order
                prev = stack.pop()
                result[prev] = i - prev #update this value in result array with the difference 
            stack.append(i)
        return result

        