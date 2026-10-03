# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
            given a bST where all nodes are unique, two nodes from the tree p and q


            return the LCA of the two nodes

            root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

            5


            root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

            3







        '''

        def dfs(node):
            if not node:
                return None
            

            if p.val == node.val or q.val == node.val:
                return node
            if p.val < node.val and q.val > node.val:
                return node
            

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node
        return dfs(root)
                
                
        