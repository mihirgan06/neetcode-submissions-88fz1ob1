# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            within a binary tree, a node x is considered good if the path from the root to the node x comtains no nodes with a value gresater than value of x

            dfs from src to target should have 0 nodes with val > target


            from src to src ==> append the count for the root node
            then recrusively explore the left and right side
            append the count





            
        '''
        count = 0

        def dfs(node, highest_seen_so_far):
            nonlocal count
            if not node:
                return 0

            if node.val >= highest_seen_so_far:

                count += 1
            highest_seen = max(highest_seen_so_far, node.val)
            dfs(node.left, highest_seen)
            dfs(node.right, highest_seen)
            return highest_seen
        dfs(root, root.val)
        return count
            
            

            


        