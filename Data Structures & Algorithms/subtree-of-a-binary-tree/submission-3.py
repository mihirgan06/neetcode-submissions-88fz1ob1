# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            given the roots of two binary trees, root and subRoot, return true if there is a subtree of rootswith the same structure and node values of subRoot

            we need to call an isSamtree helper



        '''


        def sameTree(node, subNode):
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False
            if node.val != subNode.val:
                return False
            if (node.val == subNode.val and sameTree(node.left, subNode.left) and sameTree(node.right, subNode.right)):
                return True
            return False
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))


            