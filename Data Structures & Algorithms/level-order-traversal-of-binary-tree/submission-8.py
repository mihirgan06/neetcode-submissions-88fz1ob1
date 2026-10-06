# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            Given: root
            return: level order traversal as a nested list
            each sublist contains the values of nodes at a particular level in the tree

            from left to right

            root = [1,2,3,4,5,6,7]
            [[1],[2,3],[4,5,6,7]]

            BFS
            lenq contains the number of nodes at a specific level we wanna append this as a subarray to res




        '''
        q = deque()
        if not root:
            return []

        res = []

        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

        