# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            givven root of a binary tree root
            invert the binary tree and return the root

            root = [1,2,3,4,5,6,7]
            [1,3,2,7,6,5,4]

            recursivey we want to reverse every right and left value
            dfs should reverse every node and then you call it on the lft and right subtrees


        '''
    
        if not root:
            return
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        






        