# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            given the heads of two sorted linked lists list1 and list2
            merge the two lists into one sorted linked list and return the head of the new sorted lists

            pointer for the two linked lists

            iterate through the entirety of the twoi lists
            wire between the lists based ont he values

            list1 = [1,2,4], list2 = [1,3,5]

            1 --> 1 --> 2 --> 3 --> 4 --> 5

            based ont he values of the two nodes


        '''
        #base cases: lists missing
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        curr1 = list1

        curr2 = list2
        dummy = ListNode()
        tail = dummy
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next
            
            
            
            

            

        