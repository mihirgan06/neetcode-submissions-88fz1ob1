# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
            given the roots of two binary trees p and q
            return true if the trees are equal else return false


            2 trees are equal if they share the exact same structure
            and the nodes have the same values
            p = [1,2,3], q = [1,2,3]
            same 
            p = [4,7], q = [4,null,7]
            same values but structure is diff


            p = [1,2,3], q = [1,3,2]
            same structure diff values

            recursively compare values and structure within the two trees need pointers for each tree
        '''

        
        if not p and not q:
            return True #vacuously if boith trees are empty they are equal
        if not p or not q:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        if p.val != q.val:
            return False
        if p.val == q.val and left and right:
            return True
        return False


