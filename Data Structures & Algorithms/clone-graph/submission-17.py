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
            Given: node in connected undirected graph --> return a deep copy of the grpah

            Graph is shown as an adjacency list
            Mapping nodes to lists used to represent a finite graph
            adjList = [[2],[1,3],[2]]
            [[2],[1,3],[2]]


            we intially create a copy of all the parents then of all the neighbors by dfsing on all the neighbors


        '''
        if node is None:
            return None
        oldToNew = {}
        
        def dfs(curr):
            if curr in oldToNew:
                return oldToNew[curr]
            copy = Node(curr.val)
            oldToNew[curr] = copy

            for nei in curr.neighbors:
                if not dfs(nei):
                    continue
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

            
                

            

        