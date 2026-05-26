# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            Given root --> return depth the # of nodes along the longest path from the root down to farthest leaf
            depth  = number of nodes traveled along

        '''
        if not root:
            return 0
        
        max_depth = 0
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        

        return 1 + max(left_max_depth, right_max_depth)


        


        


        