from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
            Given a graph of n nodes, and an integer n and array edges
            edges[i] = [ai, bi] indicating an edge between ai and bi in the graph
            return number of connected components

            n = 5, edges[[0,1],[1,2], [3,4]]
            0 -> 1 -> 2
            3 -> 4
            edge between 0 and 1
            edge between 1 and 2
            edge between 3 and 4

            Output = 2

            a connected component is formed when there are no disjoint subcomponents

            As in i can get from 0 to 1 to 2 nbut cant get to 3 from there so thats only one connected component

            We can DFS until we can traverse no longer then increment our count of num_components
            We need to create an adjacency list
        '''

        count = 0
        #create an empty adjacency list with space for every node

        adj = [[] for _ in range(n)]
        '''
            adj = [
            [], # neighbors of node 0
            [], # neighbors of node 1
            [], # neighbors of node 2
            [], # neighbors of node 3
            []  # neighbors of node 4
        ]
        '''
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count += 1
        return count
            
            




            
        