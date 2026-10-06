class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            given n nodes labeled from 0 to n - 1 and a list of undirected edges
            write a fucnction to check wheterh these edges make a valid tree
            n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

            0 --> 1
            \ 
              2
            how to tell if valid tree--> no cucles
            were given an undeirected graph so edges are bidirectional
            so when making our graph we need to append to both sides
            use a visited set with dfs to check if we have a cycle
            if a node is in visited and it isnt the parent --> theres a cycle its not a tree
            we alos have tp make sure the whole graph is connected so check if len(visited) == n at the end
        '''

        visited = set()
        adj_list = [[] for i in range(n)]
        for parent, child in edges:
            adj_list[parent].append(child)
            adj_list[child].append(parent)
        def dfs(node, parent):
            if node in visited:
                return False
            #add our node to visited then recurse on all its neighbors
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n
        
                

        