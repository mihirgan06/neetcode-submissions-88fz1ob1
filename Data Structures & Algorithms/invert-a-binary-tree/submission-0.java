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
    public TreeNode invertTree(TreeNode root) {
        return inverter(root);
        
    }
    private TreeNode inverter(TreeNode node){
        if(node == null){
            return null;

        }
        TreeNode tmp = node.left; //store the old left node here
        node.left = inverter(node.right); //recurse right into left
        node.right = inverter(tmp); //recurse on saved left into right
        return node;


    }
}
