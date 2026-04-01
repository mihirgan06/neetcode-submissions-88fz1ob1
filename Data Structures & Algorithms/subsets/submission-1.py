class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #potential base case of empty list
        n = len(nums)
        res = [] #will contain full answer
        sol =[] #global list we will change by appending numbers
        #start with both lists being empty
        #explore left till we hit a base case
        #upon hitting a base case backtrack and go right
        #go right and we append the right to sol, and then append sol to result
        
        def backtrack(i):
            if i == n:
                #we want a copy of solution
                res.append(sol[:])
                return
            #go down left path --> DONT pick nums at i
            backtrack(i + 1)

            #pick nums at i
            sol.append(nums[i]) #add it to sol
            backtrack(i + 1)
            sol.pop() #we want ot undo our decision at i




        
        backtrack(0)
        return res
    
        