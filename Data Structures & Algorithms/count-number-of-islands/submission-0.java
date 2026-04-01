class Solution {
    /**
    1 represents land
    0 represents water
    count and return the number of islands
    island is formed by connecting adjacent lands horizontally or verticlaly and is surrounded by water
    
    
    We need to use DFS search to solve this...
    Loop through every cell
    When you find unvisited land, launcha. DFS
    DFS spreads through the whole island, marking visited cells as waster

    */
    //Directions: down, up, right, left

    private static final int[][] directions = {{1, 0}, {-1, 0},
                                               {0, 1}, {0, -1}};
    public int numIslands(char[][] grid) {
        /**
        Scans through every cell
        if you find '1', you found the start of a new island
        Perform DFS to SINK THE ISLAND so you don't count it again
        After DFS completes, the entire island is gone --> increment islands
        Each island is counted once
        */
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if (grid[r][c] == '1'){
                    dfs(grid, r, c);
                    islands++;
                }
            }
        }
        return islands;



        
    }
    private void dfs(char[][] grid, int r, int c){
        //Boundary checks: ensures you don't fall off the grid when DFS spreads
        //If the cell is water or already visited stop
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0'){
            return;
        }
        //mark as visited

        grid[r][c] = '0';

        
        //Spread DFS in all 4 directions

        for(int[] dir : directions){
            dfs(grid, r + dir[0], c + dir[1]);
        }
    }
}
