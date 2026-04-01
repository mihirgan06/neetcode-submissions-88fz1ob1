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

/**
Balanced = every single node --> abs(height(left) - height(right) < = 1)
Height >= 0 --> means BALANCED SO FAR
height = -1 MEANS NOT BALANCED
HEIGHT IS ALWAYS GREATER THAN OR EQUAL TO 0, so -1 becomes the signal for imbalances

*/
class Solution {
    public boolean isBalanced(TreeNode root) {
        
        int helper = balanced(root);
        if(helper == -1){
            return false;
        }
        else{
            return true;
        }
    }
    private int balanced(TreeNode node){
        if (node == null){
            return 0;
            //height = 0 and balanced
        }
        int left = balanced(node.left); // get left
        int right = balanced(node.right); //get right
        int height = 1 + Math.max(left, right);
        if(left == -1) return -1;
        if(right == -1) return -1;
        if(Math.abs(left - right) > 1) return -1;
        //if unbalanced return -1
        return height;//else return real height
        
    }
}
