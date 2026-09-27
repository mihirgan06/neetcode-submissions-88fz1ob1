class MinStack:
    '''
        design a stack class with 
        - push
            append val to stack

        - pop
            remove element from stack, just stack.pop
        - top
        - getMin
            o(n) --> iterate through stack
            create an addtional stack
            we want to hold an additional stack where we only append the min elements and such that the top of the stack is the smallest element


    '''

    def __init__(self):

        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.minStack:
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

        
