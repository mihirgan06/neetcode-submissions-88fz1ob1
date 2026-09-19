# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            given root of a binary tree, return only the values of the node that are visible from the right rightSideView
        root = [1,2,3,null,4,null,5]

        if there are no nodes in the right subtree then the left subtree is visible
        so if not node.right then we can append node.left
        we unconditionally append the node value to res
        you always append the rightmost nodes uncondiitonally
        


        '''
        res = []
        def dfs(node, depth):
            if not node:
                return []
            if depth == len(res):
                res.append(node.val)

            #explore right first for right side rightSideView
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
            

            

        