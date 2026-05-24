# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            We can recursively count the L and R side, make sure the difference in nodes isnt more than 1
        '''

        def dfs(node):
            if not node:
                #base case
                return True, 0
            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)
            #this current balanced checks that the left and right subtrees make sense and tha tthe difference in levels is <= 1

            current_balanced = (
            left and
            right and
            abs(left_height - right_height) <= 1
            )
            current_height = 1 + max(left_height, right_height)

            return current_balanced, current_height
        
        return dfs(root)[0]



         


        

        


        
        

        