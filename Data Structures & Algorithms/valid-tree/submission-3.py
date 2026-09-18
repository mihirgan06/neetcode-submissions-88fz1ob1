class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            Given n nodes labeled from 0 to n - 1 and list of undirected edges
            write a function to check whether these edges make up a valid tree
            n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

            a tree is a type of graph thats acyclic
            were given an edgelist as input


        '''
        graph = [[] for i in range(n)]
        #build graph with undirected edges such that we can travel bidirectionally

        for parent,child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
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
        return dfs(0, -1) and len(visited) == n
                
            
            
        