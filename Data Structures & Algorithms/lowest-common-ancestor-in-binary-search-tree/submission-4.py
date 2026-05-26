# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, p, q):
            '''
                LCA = the lowest parent of the two nodes but the parent can be the node itself

                first if one of the nodes doesnt exist or the root doenst exist thats the base cases
                EDIT: we are told p and q will both exist


                Few different scenarios
                - say p is in the left subtree, q is in the right subtree wed want to likely return the immediate parent of both subtrees
                - what if theyre in the same subtree again the immediate parent even if thatis ione of the parents

                - We need to first find where p and q are in the tree
                - and basically handle it based off that


                USE THE BINARY SEARCH TREE PROPERTIES:
                    - if the two nodes are less than root we explore left
                    - if the two nodes are greater than root, we explore right
                    - if one is greater and one is less we can lowkey return the root i think
            '''
            if not node:
                return node
                #should just return null

            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q) #explore the left

            elif p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            
            else:
                return node
        
        return dfs(root, p, q)
            
        