"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy  = {None : None}
        #If we have a null node point it to null in the deep copy
        #matches every single old node to the copy
        cur = head
        #Pass 1:
        #Create hashmap
        #create a deep copy of each node 
        #add it to the hashmap and increment cur forward while it isnt none
        while cur:
            copy = Node(cur.val) #creates a clone/deep copy of the node andstoring it in copy
            oldToCopy[cur] = copy #maps the old node to the copy we created
            cur = cur.next
        
        #Pass 2: Pointers
        #Set the pointers for the copy node
        #The hashmap stores the copies of the pointers
        #One edge case if cur.next is nul
        cur = head
        while cur:
            copy = oldToCopy[cur]
            #two pointers for copy
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
