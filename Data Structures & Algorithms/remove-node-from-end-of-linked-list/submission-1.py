# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize a dummy node because we may end up deleting the head!
        dummy = node = ListNode()
        #in one pass we want to remove nth node starting from the end of the list
        dummy.next = head

        #we dont have a tail pointer, so we havbe to do two pointers
        slow = dummy
        fast = dummy

        #Create a fixed gap between fast and slow pointers
        #fast moves n steps ahead first then both move 1 step at a time
        while n > 0:
            fast = fast.next
            n -= 1



        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next


        


