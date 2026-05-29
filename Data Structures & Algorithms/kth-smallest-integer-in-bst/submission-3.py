# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            Given root of a BST and an integer k, return kth smallest value (1-indexed) in the tree

            We know its a BST --> everything in left subtree < node's key, everything in right side > node's key
            
            Both right and left subtrees are also BSTs

            For a kth smallest integer --> look in the left subtree first --> node --> root
            
            Inorder traversal
            - explore the left subtree 
            - then we can keep a global count var
            - decrement count ig as we explore left

        '''
        count = k
        
        def dfs(node) -> int:
            if not node:
                return None
            nonlocal count
            #explore left unconditionally
            left = dfs(node.left)

            if left is not None:
                return left
            #process current 
            count -= 1
            #if the counr is 0 we can just return the node.val
            if count == 0:
                return node.val
            
            #explore the right subtree
            
            return dfs(node.right)

        return dfs(root)


        

            
            

            
        