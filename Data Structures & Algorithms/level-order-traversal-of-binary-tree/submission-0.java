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
Level order traversal = BFS using a queue, process nodes level by level, NOT branch by branch

1. use a queue<TreeNode>
2. While the queue is not empty: each loop is a full level
3. Find out how many nodes ARE in this level
Process exactly levelSize nodes
For each node; pop from queue
Add its value toa. levelList
Add its children to queue (if not null)
Add the levelList to your final answer
*/
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        //outer list: each element = one level of a tree
        //Inner list: the values at that level from left to right
        List<List<Integer>> res = new ArrayList<>();
        //initialize result array list
        if(root == null) return res;

        Queue<TreeNode> q = new LinkedList<>();
        //offering a node to the queue essentially means we still need to process the node
        q.offer(root);//pass in the root

        while(!q.isEmpty()){
            //As long as the queue is not empty there are still unprocesed nodes
            int levelSize = q.size(); //number of nodes curr in queue
            List<Integer> level = new ArrayList<>();
            //each iteration corresponds to one entire level of the tree
            

            //Loop exactly levelSize times, guaranteeing we only proces nodes that belong to the level
            for (int i = 0; i < levelSize; i++){
                TreeNode node = q.poll();
                //remove front node of the queue assign value to node
                level.add(node.val);
                if(node.left != null){
                    q.offer(node.left);

                }
                //enqueue left and right children
                if(node.right != null){
                    q.offer(node.right);
                }
                

            }
            res.add(level);
            //add this level list to res
        }
        return res;
    }

}
