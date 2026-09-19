# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
            given a BST where all node values are UNIQUE
            two nodes from the tree p and q
            LCA between nodes p and q is the 
            [5,3,8,1,4,7,9,null,2], p = 3, q = 8
            return 5 is the LCA for both 3 and 8
            sometimes the ancestor is the descendent itself


            BST:
            - everything in the left is < root
            - everythign in the right subtree is > root

            since all values are unique we dont have to woirry about duplicates
            we are guaranteed p and q exist in the BST

            what if p or q = root.val then the LCA is always the root
            if both p and q are in the left subtree the LCA is either the root or left subtree
            same for right subtree


        '''


        def dfs(node, p, q):
            if not node:
                return
            if p.val == node.val or q.val == node.val:
                return node
            if p.val < node.val and q.val < node.val:
                #check the left subtree
                return dfs(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                #check the right subtree
                return dfs(node.right, p, q)
            if (p.val < node.val and q.val > node.val):
                return node
            if (p.val > node.val and q.val < node.val):
                return node
        return dfs(root, p, q)

                



            

        