# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            Diameter of binary tree is length of the longest oath between any two nodes       within tree



            root = [1,null,2,3,4,5]


            3

            number of edges between 1 and 5


            root = [1,2,3]

            1

        2.     3




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
        
        