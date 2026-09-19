# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            givne root
            retyrn the level order traversal as a nested lsit
            each sublist contains the values of nodes at a particular level in the tree from left and right
            root = [1,2,3,4,5,6,7]
            [[1],[2,3],[4,5,6,7]]
            append to a res list each level
            at each point the queue will hold each level of the tree


            go level by level ==> BFS



        '''
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            level_size = len(q)
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
                



        