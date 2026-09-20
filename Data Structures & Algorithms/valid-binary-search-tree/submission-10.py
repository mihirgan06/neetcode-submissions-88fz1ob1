# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ''' 
            given the root of a binary tree
            - return true if a valid isValidBST
            otherwise return false

            Valid BST iff:
            - left subtree of every node onlt nodes with keys < node's keys
            - right subtree of every node contains only nodes with keys > node's keys
            - Both the left and right subtrees are also binary search trees

            We need to ensure the properties exist for every node in the binary tree not just the first level
            so we recursively call on the lft and irhgt BSTif both are true then we know its true

        '''
        def dfs(node, low , high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return (
                dfs(node.left, low, node.val) 
                and
                dfs(node.right, node.val, high)
            )
        if dfs(root, float("-inf"), float("inf")):
            return True
        return False
        
        
        