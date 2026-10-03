# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
            you are given a binary tree, find the LCA of two given nodes ibn the tree

            LCA is defined beween two nodes p an q as the lowest node in T that has both p and q as descendants
            root = [5,3,4,2,1], p = 1, q = 2

            Output: 3
            root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12

            okay so this is a bit more difficult than the BST variation

            we cant simply check everything in booleans
            if the two nodes p and q are children of another node, return the root
            if p is the ancestor of q or vice versa return p


            
        '''
        
        def dfs(node):
            if not node:
                return None
            

            if p.val == node.val:
                return node
            elif q.val == node.val:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left if left else right
        return dfs(root)
            

            
