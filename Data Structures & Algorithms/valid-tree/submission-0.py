class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            Given n nodes (0 - n - 1) and a list of edges
            write a funciton to check whetehr these edges make up a valid tree


            It must be connected (all nodes are reachable from any other node) It must have no cycles (there's exactly one path between any two nodes)

            n = 5
            edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
            0 - 3
           / \
          4 -1  2
          every node is reachable from every point and no cycles

            n = 5
            edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]


        DFS cycle detection will likely do the trick
        '''
        if len(edges) > (n - 1):
            return False
        adj = [[] for i in range(n)]
        for u, v in edges:
            #undirected graph so edge between both means both traversable from each other
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        

            


