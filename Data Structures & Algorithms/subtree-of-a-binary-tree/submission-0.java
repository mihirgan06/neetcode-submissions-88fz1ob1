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
 Given the roots of TWObinary trees, root and subRoot --> true if there is a subtree of root with the same structure nand node values of subRoot and false othewuse
 Subtree of a binary tree is a tree that consists of a node in tree and descendants
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if(subTree(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }
    private boolean subTree(TreeNode node, TreeNode other){
        if(node == null && other == null) return true;
        if (node == null || other == null) return false;

        if (node.val != other.val) return false;
        
        return subTree(node.left, other.left) && subTree(node.right, other.right);

    }
}
