# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            Diameter of a binary tree = length of the longest path between ANY two nodes in tree
            not necessarily the root
            we must keep tryuing new paths still we find the best diameter

            length = # edges between the nodes
        '''
        res = 0 #global res
        def dfs(node):
            if not node:
                return 0
            
            nonlocal res

            left = diameterofBinaryTree(node.left)
            right = diameterofBinaryTree(node.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        dfs(root)

        return res

        