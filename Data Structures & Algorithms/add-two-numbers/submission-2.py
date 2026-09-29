# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            given two non-empty linked lists, l1 and l2, each represents a non-negative integer

            reverse order return the sum of the two numbers as a linked list


            

            edge case:
            - carry
            if the two numbers are greater than 10 we need to carry over the extra into the next ListNode
            ex: 1 --> 2 --> 3
                4 --> 5 --> 9


                5 --> 7 --> 2 --> 1
                take the ones digit and create an additional node for tens place 


                1 --> 2 --> 3
                4 --> 9 --> 5

                5 --> 1 --> 9

                321
            +   594
            _______
                915

        okay pointers for each list
        iterate through calculate sums account for carry initialized to 0
        carry will be the tens place add it to the next node if there is no next nod create a new node for it


        '''

        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        tail = dummy
        carry = 0

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            ones = total % 10
            tail.next = ListNode(ones)
            tail = tail.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return dummy.next
            
            


            
            
            
            
            
            