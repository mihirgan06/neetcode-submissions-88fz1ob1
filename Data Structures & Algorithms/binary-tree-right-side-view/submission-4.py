# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            given the root of a binary tree
            return only the values of the nodes that are visible from right side of the tree
            root = [1,2,3,null,4,null,5]
            we have both left side nodes and right side nodes
            so only the right side nodes are visible
            return [1,3,5]

            root = [1,2,3,4,null,null,null,5]

            the 1 and 3 are visible from the right side
            then we append the 4 and 5 too because there are no right subtree nodes

            we always include the root in the result
            for the right side
            no matter what depth we are always appending some sort of node to res whether thats on the left or right subtree



        '''
        res = []

        def dfs(node, depth):
            nonlocal res
            #base case no root --> return empty List

            if not node:
                return []
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            return res
        return dfs(root, 0)
        

    
            

            


        