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
class BSTIterator {
    //We need a stack to simulate recursion
    //LIFO meaning Left_> Node-> right

    Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root);


        
    }
    
    public int next() {
        //Go through the right children
        TreeNode node = stack.pop();
        if(node.right != null){
            pushLeft(node.right);
        }
        return node.val;

        
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
        //True if stack is not empty else false

        
    }
    private void pushLeft(TreeNode node){
        //pish the left node and go through entire left subtree
        //Ensures the smallest value on the top of the stack
        while(node != null){
            stack.push(node);
            node = node.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */