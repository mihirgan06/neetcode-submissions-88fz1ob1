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
    
    public boolean isValidBST(TreeNode root) {
        /**
        Given root of binary tree --> True if valid, otherwise false


        To be a valid BST
            Left subtree only contains nodes with keys less than node's key
            Right subtree only contains nodes with keys greater than node's key
            Both left and right subtrees are also BST
        */



        //First TODO: Null condition --> Null tree is a BST
        if(root == null) return true;
        //If left subtree less than root.val, and right val > root.val we would want to return true
    

        //if(root.left.val < root.val || root.right.val > root.val) return true;
        //This only checks the condition for the root, we need to iterate through the tree making sure
        //each left child of node is less than node, and each right child of node > node 

        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);


        
    }
    private boolean helper(TreeNode node, Long min, Long max){
        if(node == null) return true;
        if(node.val <= min) return false;
        if(node.val >= max) return false;
        return helper(node.left, min, (long) node.val) && helper(node.right, (long) node.val, max);
        


        
    }
}
