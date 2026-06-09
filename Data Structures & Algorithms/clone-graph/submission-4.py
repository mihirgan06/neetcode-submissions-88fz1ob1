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
            Given an adjacency list: mapping of nodes to lists of neighbors
            list = set of neighbors of a node


            AdjList = [[2], [1,3], [2]]

            1 - 2 - 3
            1 is only neighbors with 2, 2 is neighbors with both 1 and 3, 3 is neighbors with only 1


            adjList = [[]]
            if no edges then no neighbors


            Given the adjacency list we essentially recreate the graph
            We have to create the nodes like 1 - n, and create edges to the neighbors specified in the adjacency list
            

            Anytime we have a deep copy type question the goal should be to use a hashmap for the originals to copt
        '''
        #empty hashmap for mappings of old node to new ndoe
        if not node:
            return None
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            #create a copy
            copy = Node(node.val)
            #adds the copy so now the node maps to the copy
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)









        