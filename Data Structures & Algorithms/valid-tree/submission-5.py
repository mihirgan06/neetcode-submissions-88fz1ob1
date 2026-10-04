class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            given n nodes labeled from 0 to n - 1
            and a list of undirected edges
            write a function to check whetehr these edges make up a valid tre

            n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

            Undirected edges
            we have to actually create the graph from the edges
            since they are undirected we can traverse back and forth
            so for our adjacency list we can go back and forth between node and neighbor

            Were looking to detect a cycle and if all connected

            if not the parent and we see a node in visited we know its a cycle and its not a valid tree
        '''
        

        graph = [[] for i in range(n)]

        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n


            