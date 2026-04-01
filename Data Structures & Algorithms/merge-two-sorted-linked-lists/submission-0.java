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
/**
Goal: given two sorted lists, merge into one sorted list
**/
//One pointer for each list (p1 and p2)
//Whichever node has the smaller value needs to get added to the new list
//We need to walk both list simultaneously
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //Deal with the edge cases
        if(list1 == null && list2 == null){ //Both lists are empty
            return null;
        }
        if (list1 == null){ //List one is empty ==> return list 2
            return list2;
        }
        if (list2 == null){ //List 2 is empty ==> return list 1
            return list1;
        }
        ListNode dummy = new ListNode(); //where we want to store the result
        ListNode tail = dummy;
        while (list1 != null && list2 != null){
            if (list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            }else{
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        if(list1 != null){
            tail.next = list1;
        }
        if(list2 != null){
            tail.next = list2;
        }
        return dummy.next;
}
}