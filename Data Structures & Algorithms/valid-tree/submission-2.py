class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            givne n nodes labeled 0 --> n - 1 and a list of undirected edges
            whrite a function to check whetehr these edges make up a valid tree
            
             connected acyclic graph


            n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
            3
            |
            0 --> 1 --> 4
            |
            2
            no cycle
            how to detect cycle;
        '''
        graph = [[] for i in range(n)]
        for parent, nei in edges:
            graph[parent].append(nei)
            graph[nei].append(parent)
        visited = set()


        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True
        #check that we actually visited all n nodes
        return dfs(0, -1) and len(visited) == n




        