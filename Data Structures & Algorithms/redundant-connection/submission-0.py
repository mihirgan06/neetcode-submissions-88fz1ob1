class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
            given undirected graph with n nodes labeled 1 --> n
            undirected means 1 <---> 2
            we cna go back and forth
            initialy it contianed no cycles and consists of n - 1 edges

            added one additional edge to the graph
            edge has two different vertices chosen from 1--> n

            that was not an edge prev in the graph

            edge list, each edge can be traversed bidirectionally

            edges[i] = edges[i] = [ai, bi]
            edges = [[1,2],[1,3],[3,4],[2,4]]

            1 --> 2 and 2 --> 1

            1 --> 3 and 3 --> 1

            3 --> 4 and 4 --> 3
            2 --> 4 and 4 --> 2

            1 <--> 2
            |.     |
            3 < -> 4

            Union find:
            return the redundant edge
            if multiple return the last edge
            every node belongs to some connected component
            each component has a representative called its root
            for each edge [u,v] ask:
                is u and v alr in the same component
                if yes, adding the edge creates a cycle
                --> edge is redundant
            

            edges = [[1,2], [1,3], [3,4], [2,4]]

            each edge is its own parent

            parent = [0, 1, 2, 3, 4]
            parent[1] = 1
            parent[2] = 2
            parent[3] = 3
            parent[4] = 4

            find(x) should find which component x belongs to
            find(2)
            2 --> 1
            3 --> 1
            assuming 2 --> 1
            will return 1
            find(3) will also return 1

            union(u,v) merges two components
            first find their roots
            if rootU == rootV then we return False
            find(2) == 1
            find(3) == 1
            same root 
            adding another edge between them will create a cycle
            

            rank as component size initialize as 1
            for efficientcy attach the smaller tree underneath the larger tree





        '''
        n = len(edges)
        parent = [i for i in range(n + 1)]

        rank = [1] * (n + 1)
        

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            #if already connected --> cycle
            if rootU == rootV:
                return False
            
            if rank[rootU] > rank[rootV]:
                parent[rootV] = rootU
                rank[rootU] += rank[rootV]
            
            else:
                parent[rootU] = rootV
                rank[rootV] += rank[rootU]
            
            return True
        for u, v in edges:
            if not union(u, v):
                return [u,v]

        