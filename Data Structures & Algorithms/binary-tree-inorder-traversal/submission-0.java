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
    List<Integer> result = new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        //Meant to return a list of the integers we visit in inorder traversal
        if(root == null) return new ArrayList<>();
        //Create new result list
        
        //base case if the root is null return an empty list

        //Next explore the left subtree
        inorder(root);
        return result;
    }
    private void inorder(TreeNode node){
        if(node == null) return;
        inorder(node.left);
        result.add(node.val);
        inorder(node.right);

    }
    
}