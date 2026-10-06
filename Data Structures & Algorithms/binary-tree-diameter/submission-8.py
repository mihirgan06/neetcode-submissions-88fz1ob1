# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            diameter = length of the longest5 path between any two nodes within the tree

            path doesnt necessarily need to pass through root

            length of a path two nodes in a binary tree is the number of edges between the nodes


            given: root
            return: diameter


            root = [1,null,2,3,4,5]
            dfs should update the res but return up the depth


        '''
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)

            return 1+ max(left, right)
        dfs(root)
        return res