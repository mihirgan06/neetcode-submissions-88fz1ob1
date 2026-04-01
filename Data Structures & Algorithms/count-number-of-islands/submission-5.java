class Solution {
    public int numIslands(char[][] grid) {
        //Attempting to solve this problem using a BFS solution
        int rows = grid.length;
        int cols = grid[0].length;
        boolean visited[][] = new boolean[rows][cols];
        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1' && !visited[i][j]){
                    bfs(i, j, grid, visited);
                    count++;
                }
            }
        }
        return count;
        
    }
    private void bfs(int r, int c, char[][] grid, boolean[][] visited){
        
        //We need a queue to store r, c
        


        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{r,c}); //we offer in the coordinate were starting at
        visited[r][c] = true;
        
        while(!q.isEmpty()){
            int[] node = q.poll(); //empty from the queue here
            int cr = node[0];
            int cc = node[1];


            int[][] dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
            for(int[] d : dirs){
                int nr = cr + d[0];
                int nc = cc + d[1];
                if(nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length && grid[nr][nc] == '1' && !visited[nr][nc]){
                    visited[nr][nc] = true;
                    q.offer(new int[]{nr, nc});
                }
            }




        }
        return;
    }


}
