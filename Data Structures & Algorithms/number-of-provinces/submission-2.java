class Solution {
    public int findCircleNum(int[][] isConnected) {
        //n cities, some connectd some not
        //if city a is connected directly with city b and city b is connected with city c then city a is cojneted indirectly with c

        //Given nxn matrix isConnected
        //Adjacency matrix
        //if isConnected[i][j] = 1 connected, else 0
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;
        for(int i = 0; i < isConnected.length; i++){
            if(!visited[i]){
                dfs(i, isConnected, visited);
                count++;
            }
            
        }
        return count;
        
    }
    private void dfs(int node, int[][] isConnected, boolean[] visited){
        visited[node] = true;
        int numVertices = isConnected.length;
        for(int nei = 0; nei < numVertices; nei++){
            if(!visited[nei] && isConnected[node][nei] == 1){
                //if adjacency between node and neighbor
                visited[nei] = true;
                dfs(nei, isConnected, visited);
                //remember to recurse on neighbors

            }

        }
    }
}