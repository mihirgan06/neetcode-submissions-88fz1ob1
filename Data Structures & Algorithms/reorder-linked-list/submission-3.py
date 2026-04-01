# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Given head of linked list
        #reorder such that 
        #element 0, final element, 1 second to final element, ...

        #The final element of the list is the middle element
        slow = head
        fast = head
        #We want to find the middle to essentialy chop list in half
        #We are essentially reversing the second half and interweaving it with the first half
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            #this gets us safely to the middle in O(N) time
        first = head #pointer to first half of the list
        second = slow.next #pointer to second half of list
        slow.next = None
    
        prev = None

        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        while prev:
            #we need to save the original first.next and second.next in an original variable
            tmp1 = first.next
            tmp2 = prev.next
            first.next = prev
            prev.next = tmp1
            first = tmp1
            prev = tmp2

        


        