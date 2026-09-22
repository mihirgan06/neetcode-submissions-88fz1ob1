# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            given a binary tree find the LCA of two given nodes in the tree

            LCA is defined between two nodes p and q as the lwoest node in T that has both p and q as descendants

            root = [5,3,4,2,1], p = 1, q = 2

            Output: 3

            if p or q is the same as the node value we just return the node valuej


             


        '''
        def dfs(node):
            if not node:
                return
            

            if p.val == node.val or q.val == node.val:
                return node
            if dfs(node.left) and dfs(node.right):
                return node
            return dfs(node.left) if dfs(node.left) else dfs(node.right)
        return dfs(root)

            




        