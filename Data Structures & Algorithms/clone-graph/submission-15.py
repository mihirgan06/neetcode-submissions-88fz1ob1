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
            givne node in conected undirected grpah, return a deep copy of the graph

            [[2], [1, 3], [2]]


            to return a deep copy
            we need a hashmap mapping the old/og nodes to their respective copies
            we need to repeat for all hte copies of the node

            say were processing node 2
            node 2 is connected to 1 and 3
            so node2.neighbors = [1,3]

            we want to create a deep copy of [1,3]
        '''
        if not node:
            return None
        oldtoNew = {}

        def dfs(curr):
            if curr in oldtoNew:
                #if its alr in the hashmap then we just return the hashmap values for curr
                return oldtoNew[curr] 
            copy = Node(curr.val)
            oldtoNew[curr] = copy
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
                
