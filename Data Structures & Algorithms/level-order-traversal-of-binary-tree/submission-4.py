# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        '''
            level order traversal --> bFS
            keep a list for result of traversal, we need to use a BFS algorithm




        '''
        queue = deque()
        queue.append(root)
        res = []
        if not root:
            return []
        while queue:
            level = []
            level_size = len(queue) 
            #at level 1, the length fo the queue is 1 just the root we append to the queue

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

        
        