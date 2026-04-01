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
        if(node == null) return true; //null tree --> binary search tree

        //Bondary check, we need to ensure that the node value is between min and max
        
        if(node.val <= min) return false;
        if(node.val >= max) return false;
        //Call recursively ensrueing, the node.left value is BETWEEN min possible and node,val (the root would be the max for left)
        //Right subtree must be greater than node value, so the lower bound for node.right is the NODE VALUE and upper bound is the max
        return helper(node.left, min, (long) node.val) && helper(node.right, (long) node.val, max);
        


        
    }
}
