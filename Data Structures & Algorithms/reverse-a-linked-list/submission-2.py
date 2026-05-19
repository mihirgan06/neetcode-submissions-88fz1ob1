# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None #where we will point head to
        while curr:
            nxt = curr.next #create a pointer to the initial next curr points to
            curr.next = prev
            prev = curr

            curr = nxt #move curr forwartd
        return prev



        