class MinStack:
    '''
        need to implement stack
        create array and allat in the constructor

        For min stack we need another stacjk
        we want to return the minimum element from the stack
        we cant jus tlike scan through cuz we need this shit to be O(1)
        have a seperate min stack

    '''
    def __init__(self):
        self.stack = []

        self.min_stack = []

    def push(self, val: int) -> None:
        #O(1) push is jus append
        #what if its empty
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            #we only want to append to the min stack if less than the current top, so that it becomes the top
            self.min_stack.append(val)
        #i mean we need to do this regardless
        self.stack.append(val)


        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        
        

    def top(self) -> int:
        #makes sense cuz we just go to the ned of the array
        return self.stack[-1]

        

    def getMin(self) -> int:
        #need tomake this method return the top element of th min stack 

        #do we add min to the stack so that the top value is the minimum
        return self.min_stack[-1]

        
