# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            given the roots of two binary trees root and subroot
            return true if there si a subtree of root with the same structure and node values of subroot
            either node.left or node.right has to equal the subtreee
            so we recursively explore node.left and node.right at the same time as subroot
        '''
        def sameTree(node, subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            left = sameTree(node.left, subRoot.left)
            right = sameTree(node.right, subRoot.right)
            if node.val == subRoot.val and left and right:
                return True
            return False
        if not root and not subRoot:
            return False

        if not root or not subRoot:
            return False
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))
