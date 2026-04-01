# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #in order to be balanced, the height diff between the left and right subtree cannot be > 1

        if not root:
            return True
        #base case: empty tree is always balanced

        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
        
            return 1 + max(left_height, right_height)
        
        if dfs(root) == -1:
            return False
        return True