# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            To be a BST, the values in the left subtree must be strictly < node above
            To be a BST, the values in the right subtree must be strictly > node aboce
            This myst hold for the entire subtree
        '''
        def dfs(node, low, high):
            #vacously a binary search tree

            if not node:
                return True

            #immediately return false here
            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        if dfs(root, -1001, 1001):
            return True
        return False

        