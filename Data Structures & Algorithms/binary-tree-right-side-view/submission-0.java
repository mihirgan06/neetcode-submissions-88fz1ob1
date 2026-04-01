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
    public List<Integer> rightSideView(TreeNode root) {
        //We can essentially loop through the tree and only add to the arraylist the node values that are on the right subtree

        if(root == null) return new ArrayList<>();

        //null case we jsut return a blank array list
        return rightSide(root);




        
    }
    private List<Integer> rightSide(TreeNode node){
        if(node == null) return new ArrayList<>(); //handle null case we print nothing
        //we want to only add the right side values to the final result array list
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(node);
        List<Integer> result = new ArrayList<>();
    
        while(!q.isEmpty()){
            //each loop through the while is a tree level
            int size = q.size(); //number of nodes at current level
            for(int i = 0; i < size; i++){
                TreeNode curr = q.poll();
                if(curr.left != null){
                    q.offer(curr.left);
                }
                if(curr.right != null){
                    q.offer(curr.right);
                }
                if(i == size - 1){
                    result.add(curr.val);
                }
                
            }




        }
        return result;

        }



    }

