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

        def dfs(node):
            #base case no root
            if not node:
                return 0
            #start the count at 0

            nonlocal count
            #start at highest_seen

            highest_seen = node.val
            #increment the count for the root, which is always considered good
            count += 1

            if node.left.val > highest_seen:
                left = dfs(node.left)
                highest_seen = node.left.val
            if node.right.val > highest_seen:
                highest_seen = node.right.val
                right = dfs(node.right)
            return highest_seen
        dfs(root)
        return count



            



        