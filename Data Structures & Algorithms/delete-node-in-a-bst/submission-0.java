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
 3 Major Cases
 1. Case 1: Node to delete is a leaf
    If this is the case, we can just make parent point to null
2. Case 2: Node has one child
    Return the child
3. Case 3: Node has two children: Replace node's value with inorder successor = smallest valyue in right subtree*/
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return null;
        if(key < root.val){
            root.left = deleteNode(root.left, key);
        }
        else if (key > root.val){
            root.right = deleteNode(root.right, key);
        }
        else{
            //if the element is found
            if(root.left == null) return root.right;
            if(root.right == null) return root.left;
            // 2 children case
            //Find predecessor
            //copy value into current node
            int predecessor = getPredecessor(root);
            root.val = predecessor;
            root.left = deleteNode(root.left, predecessor);

        }
        return root;
        

        
    }
    

    private int getPredecessor(TreeNode node){
        TreeNode curr = node.left;
        while(curr.right != null){
            curr = curr.right;
        }
        return curr.val;
    }
}