# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            given the beginning of a linked list head, return true if there is a cycle in the list
            else return false

            thre is a cycle if at least one node in the lsit can be visited again by next pointer


            index --> index of the beginning of the cycle

            INDEX NOT GIVEN AS A PARAMETER


            slow and fast pointers

            slow --> move 1 forward at a time

            fast --> move 2 forward at a time

            if fast meets slow then we have a cycle

            [1,2,3,4] 4 points back to 2


            start slow and fast

            fast goes from 1 to 3

            slow goes from 1 to 2

            fast goes from 3 to 4 to 2
            slow is still at 2 --> cycle


        '''
        slow, fast = head, head


        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        
        