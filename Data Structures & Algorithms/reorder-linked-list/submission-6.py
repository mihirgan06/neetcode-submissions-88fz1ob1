# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            given head of a singly linked list

            positions of a linked lsit of length = 7
            [0, 1, 2, 3, 4, 5, 6]
            \
            [0, 6, 1, 5, 2, 4, 3]
            [0, n-1, 1, n-2, 2, n-3, ...]


            head = [2,4,6,8]

            [2,8,4,6]

            first node maps to last node next node maps to second to last node
            and so on
            the last node is always the middle

            3 parts:
            we find the middle
            we need to reverse the second half
            wire the nodes tgt\

            2 --> 4 
            6 <-- 8


        '''
        if not head:
            return None

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None #cut off the list

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev


        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            









        