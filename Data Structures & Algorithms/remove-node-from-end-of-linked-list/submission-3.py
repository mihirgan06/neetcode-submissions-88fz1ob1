# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            given head of a linked list and an integer n remove the nth node from the end of the list and return its head

            [1,2,3,4], n = 2

            iterate fron the right side of the list

            head = [5], n = 1
            iterate through the list
            position a pointer one node before what i need to remove






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



        
        

        