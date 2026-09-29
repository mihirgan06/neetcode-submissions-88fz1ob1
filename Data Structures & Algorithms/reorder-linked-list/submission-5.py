# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            given head of a singly linked list
            for a given length = 7:

            [0, 1, 2, 3, 4, 5, 6]


            reorder --> [0,6,1,5,2,4,3]

            [0, n - 1, 1, n - 2, 2, n - 3....]


            head = [2,4,6,8]

            [2,8,4,6]

            we need a dummy ListNode and we build our new list with tail
            we also need to reverse pointers





        '''
        if not head:
            return None
        

        #1. find the middle
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None #cut off the list


        #we now found the middle --> second

        #reverse the second half

        prev = None
        curr = second
        while curr:
            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt

        #merge the two lists
        second = prev #head of the second half of the list

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2




        



        


        

            






        



        


        