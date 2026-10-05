'''
    Implement LRU cache class
    LRU Cache(int capacity) --> intializes LRU cache of size capacity
    int get(int key) --> returns the value correspionding to the key if the key exists else -1
    void put(int key, int value) --> update the valyue of the key if it exists, otherwise add the key-value pair to the cache


    key is considered used if a get or put operation is called onto it

    once we use a key it becomes the MRU key-value
    LRU can be the left side
    MRU can be the right side

    Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

FOr get and put to be O(1) --> hashmap
to represent the MRU and LRU key-value pairs we want to use a doubly linked list

every time a key is used we remove it and move it to the right
if capacity is exceeded we remove the LRU key so remove from the left side




'''
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    

    def remove(self, node):
        #we want to remove a specified node
        prev = node.prev
        #save the previous value
        nxt = node.next
        #save the next value
        prev.next = nxt
        #wire the previous to the next value
        nxt.prev = prev
        #wire the next value back to prev
    def insert(self, node):
        #we only insert at the right side
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node
        
        
        

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #if the key is in the cache we need to return the value and move it to the right side

        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            
        

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
        
