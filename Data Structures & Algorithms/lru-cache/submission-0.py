class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    """
        LRU Cache: 
        we need to have a hashmap that stores key --> node becasue for LRU cache, the MRU node should be the right and the LRU node should be to the left


    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to node
        self.left = Node() #LRU side
        self.right = Node() #MRU side
        # connect them
        #left = LRU, right = MRU
        self.left.next = self.right
        self.right.prev = self.left
        #create the list

    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
    # insert right before self.right
        prev = self.right.prev
        nxt = self.right
        #save the next and prev node


        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node
        

    def get(self, key: int) -> int:
        #return the value for the key
        #we can find the key in O(1) using the hashmap

        #everytime we get we need to update it to the most recent apart
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1




        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #if key is alr in the cache just remove it
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



