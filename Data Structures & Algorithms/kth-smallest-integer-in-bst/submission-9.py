# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            given the root of a BST and an integer k, return the kth smallest value 1 indexed in a tree


            left subtree has only nodes with keys < node
            right subtree has nodes > node
            both the left and right are also BSTs
            root = [1,2,3], k = 1
            return the smalelst value so all the way left
            

            - start by going left and count up to k then try root then 
            


            

        '''
        res = 0
        count = 0
        def dfs(node):
            nonlocal res, count
            if not node:
                return 
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return 
            return dfs(node.right)
        dfs(root)
        return res

            

            
        