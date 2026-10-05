class MinStack:
    '''
        Stack Class:
        - push, pop, top, getMin 
        push: pushes val onto stack
        pop: removes element on the top of the stack
        top: gets the top element of the stack
        getMin: retreives the min element of the stack


        How to make getMin in O(1):
        - hold a second stack called minStack
        the top of the stack is the minimum element
        at every push if the value is < top of min stack append it to the minstack
        
    '''

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minStack[-1]
        
