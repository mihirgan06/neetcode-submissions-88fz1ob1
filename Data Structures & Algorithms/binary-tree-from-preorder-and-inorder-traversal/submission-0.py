# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
            Preorder --> node, left, right
            Inorder --> left, node, right
            we are just reconstructing the binary tree
            if preorder == inorder we just return that value


            the first value of preorder is always the root value
            we can hvae a pointer to mid within inorder

        

        '''
        if not preorder or not inorder:
            return None


        root = TreeNode(preorder[0]) #we need the entire node not just the index
        mid = inorder.index(root.val) #finds the index for the root value in the inorder array
        #everything else is a left
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid + 1]

        )
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )
        return root







        




        
            
            
            
            
        