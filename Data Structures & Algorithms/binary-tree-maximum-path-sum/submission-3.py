# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            Given: root of a non-empty binary tree
            Return: maximum path sum of any non-empty path

            Path of a binary tree is sequence of nodes where each pair of adjacent nodes has an edge connecting them
            root = [1,2,3]
            2 --> 1 --> 3
            return the sum of the node values

            root = [-15,10,20,null,null,15,5,-5]
            our max path sum can never contain a negative number
            

            dfs should create a left sum and right sum while also updatign res
            res is also updated but not returned within dfs

            wait okay clarification:
            - what if the tree is all negative we cant just reset our path sum to 0


        '''
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(res, node.val + left + right)

            return node.val + max(left, right)
        dfs(root)
        return res

            
        