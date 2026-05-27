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
        def dfs(node):
            #vacously a binary search tree
            min_value = -1000
            max_value = 1000

            if not node:
                return True
            new_max = max(node.val, min_value)
            new_min = min(max_value, node.val)
            if node.left.val >= new_max:
                return False #immediately return false
            
            elif node.right.val <= new_min:
                return False #immediately return false

            dfs(node.left)
            dfs(node.right)
            return True
        if dfs(root):
            return True
        

        