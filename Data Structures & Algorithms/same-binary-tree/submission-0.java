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
 //Given roots of two binary trees --> return true if equal, false if not
 //We can compare left and right subtrees to solve this

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return isSame(p, q);
    }
    private boolean isSame(TreeNode node, TreeNode other){
        if (node == null && other == null){
            return true;
        }
        if(node == null){
            return false;
        }
        if(other == null){
            return false;
        }
        if(node.val != other.val){
            return false;
        }
        boolean leftSame = isSame(node.left, other.left);
        boolean rightSame = isSame(node.right, other.right);
        return leftSame && rightSame;
    }
}
