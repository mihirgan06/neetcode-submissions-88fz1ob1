class Solution {
    public int findCircleNum(int[][] isConnected) {
        /** 
        n cities, some connected some not
        If city a connected directly with city b, city b connected with c --> c is connected with city c

        Province is a group of directly/indirectly connected cities and no other cities outside of the group

        Given nxn matrix isConnected, where isConnected[i][j] = 1 -> i and j are connected directly
        otherwise isconnected[i][j] = 0
        
        */

        //We could do DFS and when we find 1, explore in 4 directions
        int n = isConnected.length;
        int count = 0;
        boolean[] visited = new boolean[n];
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                dfs(i, isConnected, visited);
                count++;
            }
        }
        return count;
        
        



            
            
        }
        private void dfs(int node, int[][] isConnected, boolean[] visited){
        visited[node] = true;
        int n = isConnected.length;
        for(int i = 0; i < n; i++){
            if(!visited[i] && isConnected[node][i] == 1){
                dfs(i, isConnected, visited);
            }
        }

    }
        


        
    }
    