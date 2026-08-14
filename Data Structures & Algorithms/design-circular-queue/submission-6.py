class MyCircularQueue:
    '''
        Design and implement circular queue
        linear data structure  in which operations are performed based on FIFO

        initialize the table to be k
        MyCircularQueue(k) Initializes the object with the size of the queue to be k.

        int Front() Gets the front item from the queue. If the queue is empty, return -1.

        int Rear() Gets the last item from the queue. If the queue is empty, return -1.

        boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.

        boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.

        boolean isEmpty() Checks whether the circular queue is empty or not.

        boolean isFull() Checks whether the circular queue is full or not.

    '''

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * self.k

        self.front, self.rear = 0, 0
        self.size = 0

        
        

    def enQueue(self, value: int) -> bool:
        #enequeue --> insert where rear
        #enqueue at the end
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False #if the queue is empty return false

        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0

        

    def isFull(self) -> bool:
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