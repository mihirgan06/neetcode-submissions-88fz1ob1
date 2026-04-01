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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null){
            return;
        }
        ListNode slow = head;
        ListNode fast = head;
        //finds the middle of the linked list
        while(fast != null && fast.next != null){
            //same format as always for F&S pointers
            //These just walk the list fast and slow (2 and 1 at a time)
            slow = slow.next;
            fast = fast.next.next;
        }
        //Slow is now in the middle

        //REVERSING THE SECOND HALF
        
        ListNode prev = null; //end
        ListNode curr = slow.next; //the HEAD to the second half
        slow.next = null; //before reversing BREAK the list in half
        while(curr != null){
            ListNode tmp = curr.next;
            curr.next = prev; //point curr to null 
            prev = curr; //swap it so prev is now the new head of the second half
            curr = tmp; //move curr forward
        }
        //MERGING THE TWO HALVES
        ListNode first = head;
        ListNode second = prev;
        while(first != null && second != null){
            ListNode A1 = first.next;
            ListNode B1 = second.next;
            first.next = second;
            second.next = A1;
            first = A1;
            second = B1;
        }






        
        
    }
}
