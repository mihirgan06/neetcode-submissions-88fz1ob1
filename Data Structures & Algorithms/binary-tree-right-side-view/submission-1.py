# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            We need a way to only see whats visible on the right
            This is not always just the right children
            HOWEVER, it is only the right children if theres left children

            Make a list, do DFS if there is right child append it, if there are not right children append the left children
            Append the root unconditionally
        '''


        res = []
        def dfs(node, depth):
            if not node:
                return
            nonlocal res
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
        
            
                
        