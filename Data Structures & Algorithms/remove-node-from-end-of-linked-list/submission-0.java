/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //Given beginning of a linkedlist head and an integer n
        //Remove the nth node form the end of the list and return the beginning of the list
        ListNode dummy = new ListNode(0, head); 
        ListNode left = dummy;
        ListNode right = head;
        for (int i = 0; i < n; i++){
            right = right.next;
            //now right is n steps ahead of left
        }
        while (right != null){ //move both forward till left.next is the nodet o be deleted
            left = left.next;
            right = right.next;
        }
        //atp left is node to be deleted
        left.next = left.next.next; //delete nth node
        return dummy.next; //return the real head
        
    }
}
