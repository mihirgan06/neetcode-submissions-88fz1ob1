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
        

        dfs(root, 0)
        depth = 0 initially

        len(res) = 0
        0 == 0 so we append root of 1
        dfs(3, depth + 1)
        len(res) == 1, depth = 1
        append 3 to the depth
        dfs(2, 2)
        len(res) is 2 but depth is 3
        so it fails the if and we dont append node.left.val
        dfs()





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
            

            

        