# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            given:
            - head of a linked lsit, and integer n
            remove the nth node from the end of the list

            return the head

            head = [1,2,3,4], n = 2


            1 --> 2 --> 3 --> 4
            [1,2,4]
            remove the 2nd greatest node
            Approach:
            - two poitners fast and slow
            - start fast n nodes ahead of slow
            - when fast is at the end slow is right before the node we want to delete
        '''
        if not head:
            return None
        
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
            
        return dummy.next
        