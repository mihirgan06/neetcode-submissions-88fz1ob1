# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            given the beginning of a singly linked list head, reverse the list and return the new beginning of the list --> return head


            head =  0 --> 1 --> 2 --> 3

            return: 3 --> 2 --> 1 --> 0


            iterate throught he linked list without losing ur head reference
            so start a curr pointer at head 
            reverse all arrows
            then return curr
        '''
        curr = head
        prev = None

        while curr:
            
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt

        return prev

        