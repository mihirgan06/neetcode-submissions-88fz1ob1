class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        //Treet grid as a graph
        //set up rows and cols
        int area = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                //double looop scans entire grid
                if(grid[r][c] == 1){
                    //upon findling land, call DFS to explore entire lsland, and return the area
                    area = Math.max(area, dfs(grid, r, c));
                    //update area to the max of previous best island and current island
                    //Returning MAX area of island
                }
            }
        }
        return area;
        
    }
    private int dfs(int[][] grid, int r, int c){
        if(r < 0 || r >= grid.length || c < 0 || c >= grid[0].length) return 0;
        //Boundary check if off the left, right, off the rop, or bottom, stop immediately
        if(grid[r][c] == 0) return 0;
        //upon finding water stop exploring --> if the cell was already visited stop
        grid[r][c] = 0;
        //marks land as visited
        //visit all neighbors
        //Difference for this problem is ytou need the size of each island --> so DFS must return an int
        int down = dfs(grid, r+1, c); //down
        int up = dfs(grid, r-1, c); //up
        int right = dfs(grid, r, c+1); //right
        int left = dfs(grid, r, c-1); //left
        int curArea = 1 + down + up + right + left;
        //Current cells area + area contributed by all the connected land
        //DFS sinks and explores until boundaries or water
        return curArea;
    }
}

