# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            Given: root 
            Return: true if a valid BST

            Definition of a Valid BST:
            - every node in the left subtree is < root
            - every node in the irght subtree is > root
            - no duplicate values in this case --> COULD BE A GOOD CLARIFYING Q

            we habve to set lower and upper bounds
            we cant just compare immediate values we need to recurse and make sure every node in the right and left subtrees satisfuy the condiitons
            
        '''
        def dfs(node, low, high):
            if not node:
                return True #vacuously an empty tree IS a BST
            
            if not (low < node.val < high):
                return False
            
            left = dfs(node.left, low, node.val)

            right = dfs(node.right, node.val, high)

            return left and right
        
        if dfs(root, float('-inf'), float('inf')):
            return True
        return False
