# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #We can reverse l1 and l2 with simple reverse linked list algorithm (Part 1)

        #After that we can compute normal addition
        #Following this we can reverse the list again to get it in the intended ordr
        
        #The above approach does work, but it's not the Optimal solution


        #instead we can go straight down we dont need to reverse at all

        carry = 0
        #we only need to worry about carry if an individual sum exceeds 9


        dummy = ListNode() #this is the node for the result list

        cur = dummy
        #while neither of the lists is null
        #need to add a carry case to the loop
        while l1 or l2 or carry:
            #v1 = digit of l1 if l1 exists else its 0
            #same for v2
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit

            val = v1 + v2 + carry
            #if the number is 15, we need to extract the carry
            carry = val // 10
            #this moves the tens place of the solution over

            #this only takes the ones place for the addition
            val = val % 10
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

