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
    List<List<Integer>> result = new ArrayList<>();
    //this will store each level as a seperate sublist within result
    public List<List<Integer>> levelOrder(TreeNode root) {
        //Given root return level order traversal as a nested list
        bfs(root);
        return result;
        
    }
    private void bfs(TreeNode node){
        if(node == null) return;
        Queue<TreeNode> q = new LinkedList<>();
        //We are dealing with queues of node type
        q.offer(node);
        //essentially here create a queue and visit the node
        //level is the size of the queue
        /*
        atp the level of the queue is 0 and size is 1
        */
        while(!q.isEmpty()){
            
            int level = q.size();
            ArrayList<Integer> levelarray = new ArrayList<>();

            for(int i = 0; i < level; i++){
                TreeNode cell = q.poll();
                levelarray.add(cell.val);
                //ALWAYS Left THEN right
                if(cell.left != null){
                    q.offer(cell.left);
                }
                if(cell.right != null){
                    q.offer(cell.right);
                }
                //offer the new node
            }
            result.add(levelarray);
            
        }
    }
}
