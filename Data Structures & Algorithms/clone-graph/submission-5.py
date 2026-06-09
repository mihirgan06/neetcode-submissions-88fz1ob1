"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
            If not node --> return false
            Create hashmap of old to new nodes
            we need to create copies of the val then loop through neighbors and do the same for them add to map
            return the copy
        '''
        if not node:
            return None
        oldToNew = {}

        def dfs(curr):
            if curr in oldToNew:
                return oldToNew[curr]
            
            copy = Node(curr.val)
            
            oldToNew[curr] = copy

            for nei in curr.neighbors:
                #create copies for each neighbor
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)


            


        