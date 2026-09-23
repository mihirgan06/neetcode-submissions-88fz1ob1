# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
            given the root of a non-empty binary tree
            return the max path sum of any non emoty path
            path is a sequence of nodes where each pair has an edge connecting them
        root = [1,2,3]

        output = 6

        1
    2       3
    go from 2 to 1 to 3
    add them tgt = 6


    root = [-15,10,20,null,null,15,5,-5]
    
    max path = 15 --> 20 --> 5

    typically we wouild want to disclude negative node values?

    - we dont every revisit a node right

    - we probably want to explore right and left subtrees 



        '''
        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum
            #we want to ignore negative sums from the paths
            if not node:
                return 0
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            max_path_sum = max(max_path_sum, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return max_path_sum





    