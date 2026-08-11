class MyCircularQueue:
    '''
        Design an impleement circular queue
        FIFO last position is connected back to first position

        We need size to track the actual number of elements logiccally in the queue

    '''


    def __init__(self, k: int):
        self.k = k #capacity
        #create empty queue of size k
        self.queue = [None] * self.k
        self.front = 0
        self.rear = 0
        self.size = 0 #how many elements are logiclaly in the queue


        

    def enQueue(self, value: int) -> bool:
        #append to the end
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

        

    def deQueue(self) -> bool:
        #deletes element from the circular queue
        #if the queue is empty we cannot dequeue any elements there are no elements to remove
        if self.isEmpty():
            return False
        front = self.queue[self.front]
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

        
         


        
        
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return - 1
        return self.queue[(self.rear - 1) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        #if k elements in the queue
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()