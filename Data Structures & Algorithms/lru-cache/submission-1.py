class Node:
    #each node has a key value paur
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
        
class LRUCache:
    '''
        LRU cache initialize the LRU cacje of size capacity
        Get returns the value corresponding to the key, if key exists else return -1
        put should update the value of the key if it exists, otherwise add key-value pair to cache

        So these operations are obviously hashmap
        Input:
        ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
        capacity = 2
        pyt in pair of 1,10
        [1,10]  [2,20]  
        GET[1] --> O(1) instant lookup in constant tme
        LRU = 20 (left pointer), MRU = 10 (right pointer)
        We need that doubly linked list to reorder

        put (3, 30) 3 > capacity, we remove LRU and we can find that easily its on the left side
        make the LRU (1,10) MRU (3,30)

        Output:
        [null, null, 10, null, null, 20, -1]

        Explanation:
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 10);  // cache: {1=10}
        lRUCache.get(1);      // return 10
        lRUCache.put(2, 20);  // cache: {1=10, 2=20}
        lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
        lRUCache.get(2);      // returns 20 
        lRUCache.get(1);      // return -1 (not found

        Doubly Linked list can store the usage order the head can be MRU, the tail can be LRU
        if the cache is full we evict the LRU


    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #maps the key to nodes
        #left = LRU, right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    #remove node from list   
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev



    
    #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        



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
        if len(self.cache) > self.cap:
            #remove from list and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
