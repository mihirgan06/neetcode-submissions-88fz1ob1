# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            Given: binary tree --> find the LCA of two given nodes

            LCA is defined between two nodes as the lowest node in T that has both p and q as descendants

            root = [5,3,4,2,1], p = 1, q = 2

            output = 3
            

            we can recursively search left and right side
            if p.val == node.val or q.val then we can return that


        '''

        def dfs(node):
            if not node:
                return None
            
            if p.val == node.val or q.val == node.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            return left if left else right

        return dfs(root)