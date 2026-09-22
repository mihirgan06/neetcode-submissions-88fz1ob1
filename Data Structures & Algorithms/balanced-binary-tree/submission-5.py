# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            given a binary tree return true if it is height balanced false otherwise

            height balanced binary tree is defined as binary tree in which the lft and right subtrees if every node differ in height by no more than 1
        root = [1,2,3,null,null,4]

        traverse down left and rught subtrees
        right subtree differs by 1 so return true


        root = [1,2,3,null,null,4,null,5]

        false the right subtree goes 2 nodes deeper



        '''

        def dfs(node):
            if not node:
                #vacously height belanced
                return True, 0
            

            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)
            balanced = (left and right and abs(left_height - right_height) <= 1)
            current_height = 1 + max(left_height, right_height)
            return balanced, current_height
        return dfs(root)[0]

            
             



        