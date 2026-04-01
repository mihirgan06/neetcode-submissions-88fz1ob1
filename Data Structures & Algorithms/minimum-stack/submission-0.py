class MinStack:

    def __init__(self):
        #initialize stack as an empty array
        self.stack = [] #this allows us to create new empty minStack arrays
        self.min_stack = [] #where we define the extra empty "other" stack

        

    def push(self, val: int) -> None:
        #append value to end of stack
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop() #built-in list method
        self.min_stack.pop()


        

    def top(self) -> int:
        #top of stack is the last element of array
        return self.stack[-1]
        

    def getMin(self) -> int:
        #brute force solution would be to loop through stack for the minimum
        #whats the efficient way to do this problem?
        return self.min_stack[-1]
        
        
        
