# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            given the root of a binary tree return its depth

            depth of binary tree is defined as number of nodes along the longest path from the root down to farthest leaf node

          root = [1,2,3,null,null,4]
            1
          /. \
        2     3
             /
            4

         
        '''
        if not root:
            return 0
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
        