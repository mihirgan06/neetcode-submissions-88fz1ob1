# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            given a binary tree root
            reutrn the level order traversal of it as a nested List

            each sublist contains the values of node at a particular level in the tree
            explore level by level at the end of the level append the entire level as an array to our res

            BFS
            the queue holds the entire level within
            

        '''
        res = []
        if not root:
            return []

        q = deque()
        q.append(root)

        while q:
            level = []
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
            

        