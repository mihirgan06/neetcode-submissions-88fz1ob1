# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
            This problem requires a dummy node
            You cant create a new entire list, you just habve the dummy node and have it point to the head
            the head is just the head of the list and then you route that to point to the last node, 
            the last node then points to the next node which points ot the second to last node


            Dont use the above approach: if we wanted to use a dummy ndoe we would end up having to loop to find the end of the list

            Alternative approach:
            - Find the mdidle
            - reverse the second half
            - merge/inter.eave the two halves

        '''

        #1. Find the middle

        slow, fast = head, head
        while fast.next and fast.next.next:
            #gets slow to the end of the first half
            #move slow and fast
            #at the end of this slow is at the middle
            slow = slow.next
            fast = fast.next.next
        second = slow.next #pointer to the second half
        #cut list
        slow.next = None 

        #2. Reverse the second half
        #second points to the first node of the right half
        prev = None
        curr = second
        while curr:
            nxt = curr.next #where to go next
            curr.next = prev #reverse the arrow
            prev = curr#move prev forward
            curr = nxt #move curr forward
            #repeat wiule curr exists
        
        #3. Interleave

        first = head #points to first half of list
        #we just interleave the lsits
        while prev:
            temp1 = first.next
            temp2 = prev.next
            first.next = prev
            prev.next = temp1
            first = temp1
            prev = temp2
        
    

        


        

            




        