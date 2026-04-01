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
    public boolean hasCycle(ListNode head) {
        /**
        given head of linked list, return true if cycle
        Cycel is defined when at least one node in the list can be visited again
        **/
        int index;
        ListNode slow = head;
        ListNode fast = head;
        if (head == null || head.next == null) {
            return false;
        }
        
        while(fast != null && fast.next != null){
            slow = slow.next; //Iterates through list slowly one node at a time
            fast = fast.next.next; //Will iterate through the list at twice the spped of slow pointer (2 nodes at a time)
            if (slow == fast){
                return true;
            }
        
        }
        return false;

        
        
    }
}
