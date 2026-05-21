# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Ok given the lists in reverse order we return in reverse order dont htink too much about this prob but it matters for carry
            If we get the case of the carry we represent the ones place first and wire it to the tens position

            EX:
            9 + 9 = 18 which we represent as 8 --> 1
            Without carry:
            1 --> 2 --> 3 + 4 --> 5 --> 6 = 5 --> 7 --> 9


            Lets handle the case without carry first

            pointer to head of both lsits
            iterate through both add each value and store in a new node
        


        '''

        curr1, curr2 = l1, l2
        dummy = ListNode()
        tail = dummy
        carry = 0

        while curr1 or curr2 or carry:
            
            #have to account for the edge of case of one of the lists being null
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            total = val1 + val2 + carry #store the pure val of the addition
            #carry case

            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return dummy.next
        






