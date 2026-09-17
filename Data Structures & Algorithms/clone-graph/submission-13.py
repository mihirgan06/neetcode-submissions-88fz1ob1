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

            given a node in a connected undirected graph
            return a deep copy of grpah'

            create a copy of the node then for all the neioghbors 
            dfs is what creates the copy


            [[2], [1,3], [2]]


            node 1 --> [2]
            node 2 --> [1,3]
            node 3 --> [2]
        '''
        if not node:
            return None
        oldtoNew = {}
        def dfs(curr):
            if curr in oldtoNew:
                #we already have a copy
                return oldtoNew[curr]
            copy = Node(curr.val)
            oldtoNew[curr] = copy
            
            
            for nei in (curr.neighbors):

                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
                

