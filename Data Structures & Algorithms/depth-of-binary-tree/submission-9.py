# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      '''
        given root of a binary tree return its maxDepth

        depth of a binary tree is defined as the number of nodes along the longest path from root to farthest leaf node
        this is either in the right subtree, so essentially we are returning the max of that\
      '''
      if not root:
        return 0
      

      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
      

        