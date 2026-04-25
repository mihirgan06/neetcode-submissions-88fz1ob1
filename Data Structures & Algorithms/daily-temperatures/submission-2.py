class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Given array of temepratures where temperatures[i]
            daily temperatures on the ith day

            result = array where the i refers to the number of days before a warmer temp appears
            
            if no watmer temp for an ith day put in 0



            Approach: O(N)

                We could use a stack, push first value, iterate throiugh temperatures, if the next value is greater pop and replace iwth the number of indices till the larger temp
        '''
        stack = []
        result = [0] * len(temperatures)
        #result[i] = the number of days after the ith day before a warmer temperature appears on a future day
        #if theres no day in future with a warmer temperature set result[i] = 0

        for i, temp in enumerate(temperatures):
             #append each value to the stack
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
            

        return result



