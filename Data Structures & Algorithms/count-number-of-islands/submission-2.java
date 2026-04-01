class Solution {
    int count = 0;
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == '1' && visited[r][c] == false){
                    count++;
                    dfs(grid, r, c, visited);
                }
            }
        }
        return count;

        
    }
    private void dfs(char[][] grid, int r, int c, boolean[][] visited){

        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length) return; //boundary check
        if(grid[r][c] == '0') return;
        if(visited[r][c]) return;
        visited[r][c] = true;
        //these are all the checks we want
        dfs(grid, r + 1, c, visited);
        dfs(grid, r-1, c, visited);
        dfs(grid, r, c+1, visited);
        dfs(grid, r, c - 1, visited);


    }
}
