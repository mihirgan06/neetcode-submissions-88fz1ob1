# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Iterative Approach:
            #root is null --> return root value because it is by definition he kth smallest elem
            #
            #
        n = 0
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            #we processed a node increment n
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

        