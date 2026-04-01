class Solution {
    /**
    There are n cities, some are conected, some are not. 
    If city a connected with city b and city b is connected with city c, city a connected with city c
    2D matrix to represent (nxn)
    province = group of directly or indirectly connected cities




    My Approach:
    We can use DFS to scan the entire grid, and see if cities are connected. If nxn is 1 it means its a city, and if horizontally/vertically connected to another 1 its a province
    */
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length; //n = number of cities
        boolean[] visited = new boolean[n]; //create visited boolean array with the set length of the 2D matrix
        int count = 0; 
        for (int i = 0; i < n; i++) { //Loop over every city
            if (!visited[i]) {
                count++;                   // new component
                dfs(i, isConnected, visited); // explore this component
            }
        }
        return count;



        
    }
    private void dfs(int node, int[][] isConnected, boolean[] visited){
        visited[node] = true; //start by marking the city as visited preventing revisits
        for(int v = 0; v < isConnected.length; v++){
            if(isConnected[node][v] == 1 && !visited[v]){
                dfs(v, isConnected, visited);
            }
        }

    }
}