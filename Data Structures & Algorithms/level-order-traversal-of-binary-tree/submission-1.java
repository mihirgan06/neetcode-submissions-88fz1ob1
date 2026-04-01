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
    public List<List<Integer>> levelOrder(TreeNode root) {
        //Given a binary tree root --> level order traversal as a NESTED LIST

        //each sublist contians VALUES of nodes at a particular level
        List<List<Integer>> result = new ArrayList<>();

        if(root == null) return new ArrayList<>(); //Handle base case of the root being NULL --> empty list

        //We're essentially performing a BFS, meaning we NEED a queue

        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        //mark the root asvisited so we don't process it again
        while(!q.isEmpty()){

            int size = q.size();
            List<Integer> subresult = new ArrayList<>();

             //set the size = level 
            //check if left and right exist
            //If so offer it to the queue
            
            for(int i= 0; i < size; i++){
                TreeNode node = q.poll();
                subresult.add(node.val);
                if(node.left != null){
                q.offer(node.left);
                }
                if(node.right != null){
                    q.offer(node.right);
                }
            }
            result.add(subresult);
            
        }
        return result;



        
    }
}
