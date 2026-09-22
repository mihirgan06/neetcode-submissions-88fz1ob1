# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            diameter of binary tree as the length of the longest path between any two nodes


            path doesnt necesarrily need to go through the root

            length is the number of edges between the nodes

            given the root return the diameter of the tree


        '''
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            
            left = dfs(node.left)
            right = dfs(node.right)


            res = max(res, left + right)

            return 1 + max(left, right)
        dfs(root)
        return res

            
            

            
        