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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //Given the roots of TWO binary trees p and q 
        //Return true if the trees are equal, false otherwise

        
        //Both null -> return true
        if(p == null && q == null){
            return true;
        }
        //One is null -> must be false
        if(p == null){
            return false;
        }
        if(q == null){
            return false;
        }
        if(p.val != q.val) return false;
        
    

        //so we wanna recurse through each subtree and compare each node
        boolean leftSame = isSameTree(p.left, q.left);
        boolean rightSame = isSameTree(p.right, q.right);
        return leftSame && rightSame;

        

        
    }
    
}
