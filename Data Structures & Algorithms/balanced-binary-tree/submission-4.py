# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            givne a binary tree
            return true if it is height balanced
            height balanced binary tree is defined as a binary tree in which the left and right subtrees cannot differ in height by more than 1


            find the left depth
            right depth
            ensure that the difference in depths is NOT > 1


        '''


        def dfs(node):
        #dfs should return if balanced and the height 
            if not node:
                return True, 0
            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)
            balanced = (left and right and abs(left_height - right_height) <= 1)
            current_height = 1 + max(left_height, right_height)
            return balanced, current_height
            

        
        return dfs(root)[0]


        