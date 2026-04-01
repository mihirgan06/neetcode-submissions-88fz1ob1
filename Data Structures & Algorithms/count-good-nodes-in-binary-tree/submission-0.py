# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #a node's value is considered GOOD if no value in the path to it is greater than it

        count = 0
        max_so_far = 0
        if not root:
            return 0
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            count = 0
            if node.val >= max_so_far:
                count = 1
            new_max = max(max_so_far, node.val)
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)