# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
            given the root of binary search tree and a value to insertIntoBST
            return the root after the insertion
        '''
        #create a new node
        node = TreeNode(val)
        #empty root --> root = node
        if not root:
            root = node
            return root
        

        if node.val < root.val:

            root.left = self.insertIntoBST(root.left, val)

        elif node.val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        
        

        



            
            