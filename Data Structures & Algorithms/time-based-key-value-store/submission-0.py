class TimeMap:
    '''
        Design a time-based key-value data structure: multiple values for the same key at diff timestamps and retrieve the key's value at certain timestamp

        First initialize this shit, i mean key value im initaliy thinijngw e need a hashmap


    '''

    def __init__(self):
        self.store = {} #we intialize a key to list that will store val, time
        #key = string, value = [list of [value, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #stores the key key with the value value at the given timestamp
        if key not in self.store:
            self.store[key] = [] #append an empty list if its alr in the list
        self.store[key].append([value, timestamp])
     

    def get(self, key: str, timestamp: int) -> str: #logn op
        #returns a value such that set was called prev with timestamp_prev <= timestamp
        #if it cannot find it it just returns ""
        #returns the value, if there isnt a value assigned to a number just return the opne at the prev timestamp
        #the timestamps are inc order, so we can just binary search the timestamps
        res = ""
        #this actually checks what the get is
        values = self.store.get(key, [])
        #binary search
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            #check the second val which is our timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0] #DO NOT APPEND ITS A STRING DUMMY
                l = mid + 1
            else: #value is too big
                r = mid - 1



        return res


        

        
