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
            Given a node in a connected undirected graph, return a deep copy of the graph
            adjacency list = mapping of nodes to lists where each list is the list of neighbors

            Nodes numberd from 1 to n where n is the total number of nodes in the graph
        '''

        oldToNew = {}
        if not node:
            return
        def dfs(curr):
            #first create a copy
            if curr in oldToNew:
                return oldToNew[curr]
            #create a copy node
            copy = Node(curr.val)
            oldToNew[curr] = copy
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

            
        
        