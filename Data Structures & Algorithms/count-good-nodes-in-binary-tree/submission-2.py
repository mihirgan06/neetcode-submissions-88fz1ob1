# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ''''
            a node x is good iff the path from the root to the node has no intermediate nodes with values > x
            The value of x must be > root and every other ndoe in between for the path

            Intuition;
                DFS approach, we cna recursively check whetehr we have seen a greater nide when going toi a path
                Once we classify a node as good, we have to restart our search

        '''''
        count = 0
        

        def dfs(node, highest_seen_so_far):
            #base case no root
            if not node:
                return 0
            #start the count at 0

            nonlocal count

            #increment the count for the root, which is always considered good
            if node.val >= highest_seen_so_far:

                count += 1
            highest_seen = max(highest_seen_so_far, node.val)


            dfs(node.left, highest_seen)
            dfs(node.right, highest_seen)
            return highest_seen
        
        dfs(root, root.val)
        
        return count



            



        