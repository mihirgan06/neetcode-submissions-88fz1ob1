/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int count = 0;
    int result = -1;
    //Initiualize these outside variables outside because recursion restarts local variables on every recursive call
    
    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;

        
    }
    private void inorder(TreeNode node, int k){
        //base case
        if (node == null){
            return;

        }
        //Left first
        inorder(node.left, k);
        count++;
        //Root next 
        if (count == k){
            result = node.val; //save this root's value
            return;
        }
        inorder(node.right, k); //right
        
    }
}
