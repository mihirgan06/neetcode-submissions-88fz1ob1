# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            Ok the n is 1-indexed meaning removing when n = 1 means removing the last node
            we will need a pointer at the end of the list, we cant access the end in O(1) bc theres no tail pointer
            Use a diummy node here bc we may need to remove the head

        '''
        dummy = ListNode()
        dummy.next = head
        #MAY need to remove head so need a dummy node
        l, r = dummy, head
        for i in range(n):
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
            



