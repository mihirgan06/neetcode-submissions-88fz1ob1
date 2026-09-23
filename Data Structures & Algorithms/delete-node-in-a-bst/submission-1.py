# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
            given a key delete the node with the given key in the BST if present

            3 cases:
            1. 0 children --> just remove the node
            2. 1 child --> replace with the child
            3. 2 children --> replace with inorder/preorder successor



        '''
        #nothing if the root is empty
        
        

        
        if not root:
            return
            
        #search portion
        if key < root.val:
    
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                successor = root.left
                while successor.right:
                    successor = successor.right
                root.val = successor.val
                root.left = self.deleteNode(root.left, successor.val)
        return root


        






        


        