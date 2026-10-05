# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
            given:
            - beginning of a list head, return true if there is a cycle
            else return false


            slow and fast pointer approach
            head = [1,2,3,4], index = 1

            start slow and fast at the head
            slow moves one pointer at a time
            fast moves two pointers at a time

            when slow is at 1 fast is at 3
            since theres a cycle 
            when slow is at 2 fast is back at 2

        '''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        