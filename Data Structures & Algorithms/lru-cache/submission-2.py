class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    '''
        class should support following operation
        LRUCache(int capacity)
        int get(int key) --> return the value correspomding to the key

        else return -1


        put(int key, int value) --> update the value of the key if the key exists, otherwise add the key-value pair to the cache


        ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]


        get and put are obv O(1) for a hashmap


        if we put in a va;lue and its > capacity --> we need to kick out the LRU
    to remove/insert doubly linked llists give O(1) removal/insertion


    MRU items go near one end
    LRU items sit on the other end
    left side = LRU
    right side - MRU
    LRU                                 MRU
    left dummy <--> node <--> node <--> right dummy

    insert helper:
    1. if you call get(B) B became most recently used
        a) remove B from the middle
        b) insert it near the MRU side
    remove helper
    called to detach the node from wherever it currently ius
        

        

    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

        


    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            #remove from list and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
