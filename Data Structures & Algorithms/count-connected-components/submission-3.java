class Solution {
    public int countComponents(int n, int[][] edges) {
        //edges array: edges[i] = [a,b] means edge between a and b
        List<List<Integer>> adj = new ArrayList<>();
        int count = 0; //initalize counter
        boolean[] visited = new boolean[n];
        //create boolean array
        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
            //create adjacency list
        }
        for(int[] e : edges){
            //add edges
            int a = e[0];
            int b = e[1];
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                count++;
                dfs(i, visited, adj);
            }
        }
        return count;
        
        

    }
    private void dfs(int node, boolean[] visited, List<List<Integer>> adj){
        //boolean visited = number of components
        int count = 0;
        visited[node] = true;
        for(int nei: adj.get(node)){
            if(!visited[nei]){
                dfs(nei, visited, adj);                

            }


        }
        return;

    }
}
