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
Conditions for valid BST
* left subtree of every node ONLY contains codes with keys less than the nodes key
* right only greater
* both left and right are also binary
Validate BST Logic (Min/Max Recursion Pattern):

Each node has an allowed value range: (min, max)

Root starts with (−∞, +∞)

For left child → new max = node.val

For right child → new min = node.val

If a node’s value falls outside the range → NOT a BST

Recursively check entire tree
*/
class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE,Long.MAX_VALUE );
        
    }
    private boolean valid(TreeNode node, long min, long max){
        if(node == null){
            return true;
        }
        if(node.val <= min || node.val >= max) return false;
        return valid(node.left, min, node.val) && valid(node.right, node.val, max);
        
}
}