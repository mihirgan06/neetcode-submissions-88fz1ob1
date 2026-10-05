# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            given the beginning of singly linked list head, reverse the list and return the new beginning of the list


            head = [0,1,2,3]
            output = [3,2,1,0]
            we want to reverse the arrows


            start curr at the head
            save the next pointer 
            move the arrow then move curr to be the nxt node


            prev --> 0 --> 1 --> 2 --> 3

            

        '''

        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

