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
    public int maxDepth(TreeNode root) {
        //given a root return the depth
        //depth of a binary tree is defined as the number of nodes
        return depth(root);


    }
    private int depth(TreeNode node){
        if (node == null){
            return 0;
        }
        else{
            int left = depth(node.left);
            int right = depth(node.right);
            return 1 + Math.max(left, right);

        }
    }   
}
