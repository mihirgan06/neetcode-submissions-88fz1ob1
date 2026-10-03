# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
            given the root of a binary tree, return true if its a valid isValidBST
            else reutrn false


            - left usbtree contains only nodes with keys < node keys
            - right subtree of every node contains only nodes with keys > node
            - both left and right subtrees are also BSTs
            root = [2,1,3]

            root, left, right
            root = [1,2,3]
            false

            the left subchild > root



        '''

        def dfs(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            #if we dont have a valid node value

            left = dfs(node.left, low, node.val)

            right = dfs(node.right, node.val, high)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
            

        