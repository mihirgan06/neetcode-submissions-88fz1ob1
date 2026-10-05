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
        '''
            Given:
                head of a linked lsit with length n
                each node contains an additional poitner random may pointe anywehre in the list or null
            create a deep copy of the list
            deep copy --> exactly n new nodes

            - original value val 
            next pointer corresponding to node.next
            - random pointer corresponding to node.random
            Create a hashmap and then iterate through the list and copy over all the pointers save them and point it in our hashmap
            First save the newNodes
        '''
        if head is None:
            return None

        oldToNew = {}
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        

        curr = head
        
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew.get(curr.next)
            copy.random = oldToNew.get(curr.random)
            curr = curr.next
        return oldToNew[head]


        