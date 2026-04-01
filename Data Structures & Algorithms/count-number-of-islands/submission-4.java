class Solution {
    public int numIslands(char[][] grid) {
        //Given a 2D grid where '1' represents land and '0' represents water
        //We want to count and return number of islands
        //islands spread from 1 in 4 directions
        //So when we find a 1, we should explore all 4 directions
        int count = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++ ){
                //here i and j are the cooredinates of the cells
                if(grid[i][j] == '1' && !visited[i][j]){
                    dfs(i, j, grid, visited);
                    count ++;
                }
            }
        }
        return count;

        
    }
    private void dfs(int r, int c, char[][] grid, boolean[][] visited){
        //Every point on this grid has a coordinate (r, c)
        //we want to mark the top left for ex. as visited so we can mark[r][c] as visited 
        if(r < 0 || r >= grid.length || c < 0 || c >= grid[0].length){
            return;
        }
        if(grid[r][c] == '0' || visited[r][c]){
            return;
        }
        
        if(grid[r][c] == '1' && !visited[r][c]){
            visited[r][c] = true;
            dfs(r + 1, c, grid, visited);
            dfs(r, c + 1, grid, visited);
            dfs(r - 1, c, grid, visited);
            dfs(r, c - 1, grid, visited);
        }
        
        
        
        return;

    }
}
