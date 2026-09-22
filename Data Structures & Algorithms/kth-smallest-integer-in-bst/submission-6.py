# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            given the root of a bst, and an integer k, return the kth smallest value in the tree

            left subtree --> only nodes with keys less than the node's keys

            right subtree --> nodes with keys > node's keys

            both the left and right subtrees are also BSTs
            root = [2,1,3], k = 1

            inorder traversal:
            - left, process node, right side

            process node can be incrementing our count variable
            when count == k we can return the node val

        '''

        count = 0
        res = 0

        def dfs(node):
            nonlocal count
            nonlocal res
            #if no root then we return nothing because its impossible to return the kth largest integer
            if not node:
                return
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
            

        