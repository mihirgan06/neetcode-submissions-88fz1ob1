# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            given root of a binary search tree and an integer k, return the kth smallest value in the tree

            - left subtree of every node contains onlt nodes with kets less than the node's key
            - right subtree of every node contains omnly nodes greater than the node's key

            both the left and right subtrees are also binary search trees

                root = [2,1,3], k = 1

                return the smallest value in the tree, since its a bst go left, since its k = 1 it wouold be the left most value

                root = [4,3,5,2,null], k = 4
                would be the largest value since theres oly 4 values

                we need to traverse the tree comparing the values


                inorder traversal:
                - left, node, right
             
            inorder = 2, 3, 4, 5, 7, 8
            left node right



        '''
        count = 0
        ans = 0
        def dfs(node):
            nonlocal count
            nonlocal ans
            if not node:
                return
            dfs(node.left)
            #processing root
            count += 1
            if count == k:
                ans = node.val
                return
            return dfs(node.right)
    
        dfs(root)
        return ans

            

            

            