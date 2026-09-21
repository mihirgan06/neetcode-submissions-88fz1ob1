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
            root = [5,3,4,2,1], p = 1, q = 2

            return 3

            this isnt as easy as BST because we arent guaranteed when to check left and right side

            the left side isnt necessarily < node and the right side isnt necessarily > root


            root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12

            3 because 3 is hte lCA of 3 and 12
            we likely unconditionally explore 
            if node is p or node is q --> return node

        '''

        def dfs(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left if left else right
        return dfs(root)


        
            


        