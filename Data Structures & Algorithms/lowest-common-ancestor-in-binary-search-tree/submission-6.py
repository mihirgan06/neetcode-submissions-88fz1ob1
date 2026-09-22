# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
            given a BST where all node values are unique
            two nodes from the tree p and q
            return the LCA of the two nodes
            LCA between two nodes p and q is the lowest node in the Tree such that both p and q are descendants

            root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
            the LCA would be 5

            condition 1:
            - if one node is on the left side and the other is on the right side then we can say that the LCA is the node values
            - root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
            if the nodes are in the same tree then we should return p/q
            so if p or q = the node were recursing on we return that node values

            because this is a BST

            - everything less than the node value is on the left side
            - everything greater than the node value is on the right side



        '''

        def dfs(node):
            if not node:
                return
            
            if p.val == node.val or q.val == node.val:
                return node

            elif p.val < node.val and q.val < node.val:
                #we search the left side
                return dfs(node.left)
            
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node
        return dfs(root)

            
        