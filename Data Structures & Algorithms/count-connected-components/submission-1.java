class Solution {
    /**
    We have an undirected grpah with n nodes. There is also an edges array where edges[i] = [a,b]
    This means there is an edge between node a and node b in the graph

    When do I Need an Adjacency List
    * When you see a problem with Nodes AND edges [u,v] --> Adjacency list
    

    */
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>(); //create a new adjacency list
        //Next we have to populate it
        for(int i = 0; i < n; i++){
            //adds spots for n nodes
            adj.add(new ArrayList<>());
        }
        //next we have to populate it with edges
        for(int[] e : edges){
            int u = e[0], v = e[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        boolean[] visited = new boolean[n];
        int count = 0;
        for(int node = 0; node < n; node++){
            if(!visited[node]){
                count++;
                dfs(node, adj, visited);
            }
        }
        return count;

    }
    private void dfs(int node, List<List<Integer>> adj, boolean[] visited){
        if(visited[node]) return;
        visited[node] = true;
        for(int neighbor : adj.get(node)){
            dfs(neighbor, adj, visited);
        }
    }
}
