# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            given a binary tree, return true if it is height balanced and false otherwise

            height balanced binary tree = binart ree in which left and right subtrees of every node differ in height by no more than 1

            root = [1,2,3,null,null,4]

            dfs should return the height and then we check if the height difference > 1 return false if it is else true
            dfs should return boolean + height

        '''
        

        def dfs(node):
            if not node:
                return True, 0
            
            
            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)
            balanced = (left and right and abs(left_height - right_height) <= 1)
            current_height = 1 + max(left_height, right_height)
            return balanced, current_height
        return dfs(root)[0]
            
            

            




        