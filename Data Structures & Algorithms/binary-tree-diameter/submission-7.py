# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
            diameter of a bianry tree is = length of the longest path between any two nodes within the tree


            DOESNT NECESSARILY hvae to pass through the root

            length of a path between two nodes in a binary tree is the number o fedges between the nodes

            given the root return diameter

            root = [1,null,2,3,4,5]

            3

            dfs(node) --> returns the height of a subtree rooted at node





        '''
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter

        