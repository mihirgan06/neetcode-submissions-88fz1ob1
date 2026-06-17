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
            each node has an integer value with lsit of neighbors
            we need to return a deep copy of the graph
        '''
        if not node:
            return None

        path = []
        oldToNew = {}
        
        def dfs(curr):
            if curr in oldToNew: 
                #if we already have a clone return that clone
                return oldToNew[curr]
            #create a copy of our node
            copy = Node(curr.val)
            #map our current node to the copy
            oldToNew[curr] = copy
            for nei in curr.neighbors:
                #return copy for each of the neighbors
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)


            
            

        