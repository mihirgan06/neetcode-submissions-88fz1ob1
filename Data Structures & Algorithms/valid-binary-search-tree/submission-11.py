# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            given the root of a binary tree return true if valid isValidBST
            valid BST:
                - everything int he left subtree contains only nodes with keys < node's keys
                - right subtree of everynode contains only nodes with keys greater than node's key

                - both the left and right subtrees are also BSTs
                root = [2,1,3]

                return true
                2
            1       3
            return true

            1
          2  3
          false
          left subtree has nodes > root





        '''


        def dfs(node, low, high):
            #base case: vacuously a BST if no root
            if not node:
                return True
            if not low < node.val < high:
                return False
            return (dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high))
            

        return dfs(root, float("-inf"), float("inf"))


            
            
            


        