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
            Each node has a next and random pointer
            the random pointer can either go to a different node or to null
            Aiming for O(N) time and space we need to create an identical new list

            1. Create a new linked list
            2. iterate through the existing list
            3. Keep a hash table of where the old list maps to copy
            4. replicate those pointers and return
        '''

        oldtoCopy = {None: None}
        curr = head

        while curr:
            oldtoCopy[curr] = Node(curr.val)
            curr = curr.next

        #as of now weve stored mappings of the original nodes to copies with the smae val

        #pass2: we need to store all the ptrs

        curr = head
        while curr:
            copy = oldtoCopy[curr]
            copy.next = oldtoCopy[curr.next]
            copy.random = oldtoCopy[curr.random]
            curr = curr.next
        return oldtoCopy[head]

            



        