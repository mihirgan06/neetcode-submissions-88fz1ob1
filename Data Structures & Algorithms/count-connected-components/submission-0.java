/**
Connected components: seperate group
SO essentially returns the number of unique components between a list given n number of nodes
Here we have an adjacency list, uses visited[]
*/
class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n; i++){
            //adding spots for n nodes
            graph.add(new ArrayList<>());
        }
        //Next populate it with edges
        //because it is undeirected, add in both directions
        //get(u).add(v)
        for(int[] e : edges){
            int u = e[0], v = e[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        boolean[] visited = new boolean[n];
        int count = 0;
        for(int node = 0; node < n; node++){
            if(!visited[node]){
                count++;
                dfs(node, graph, visited);
            }
        }
        return count;

    }
    private void dfs(int node, List<List<Integer>> graph, boolean[] visited){
        if (visited[node]) return;
        visited[node] = true;
        for(int neighbor : graph.get(node)){
            dfs(neighbor, graph, visited);
        }

    }
}
