class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        boolean[][] visited = new boolean[rows][cols];
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == '1' && !visited[r][c]){
                    dfs(r, c, grid, visited);
                    count++;
                    
                }
            }
        }
        return count;
        
    }
    private void dfs(int r, int c, char[][] grid, boolean[][] visited){
        //boundary checks
        if(r < 0 || r >= grid.length || c < 0 || c >= grid[0].length){
            return;
        }
        

        //if water or we visited the coordinate return
        if(grid[r][c] == '0' || visited[r][c]) return;


        visited[r][c] = true;
        dfs(r + 1, c, grid, visited);
        dfs(r - 1, c, grid, visited);
        dfs(r, c + 1, grid, visited);
        dfs(r, c - 1, grid, visited);

    }
}
