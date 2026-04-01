# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        prev = None
        #Approach:
        #Iterate through list while curr is valid
        #at each node reverse the arrow then move curr forward
        while curr:
            #prev node points to the null space prior to the head          
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


            
        


        
        