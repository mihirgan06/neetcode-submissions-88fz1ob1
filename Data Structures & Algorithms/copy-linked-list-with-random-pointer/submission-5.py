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
            given a head of a linked list n

            each node contains and additional random pointer 
            return a deep copy of the list


            hash map needed to map old to new nodes we want to save the wiring for the original list

            then build our new linked list based off our hashmap VALUES

        '''
        if head is None:
            return None

        oldtoCopy = {}
        curr = head

        while curr:
            #populate the hashmap with a new node with the same value
            oldtoCopy[curr] = Node(curr.val)

            curr = curr.next
        curr = head
        while curr:
            copy = oldtoCopy[curr]
            copy.next = oldtoCopy.get(curr.next)
            copy.random = oldtoCopy.get(curr.random)
            curr = curr.next
        return oldtoCopy[head]
        


        