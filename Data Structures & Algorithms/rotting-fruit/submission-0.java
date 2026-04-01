class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int time = 0;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                //Scan through entire grid
                //collects the initial rotten first
                if(grid[r][c] == 2){
                    queue.offer(new int[]{r, c});
                }
                //increments and counts the frsh
                if(grid[r][c] == 1){
                    fresh++;
                }

            }
        }
        //Edge Case: no fresh oranges
        if(fresh == 0) return 0; 
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        //BFS

        while(!queue.isEmpty()){
            int size = queue.size();
            boolean rottedThisMinute = false;

            for(int i = 0; i < size; i++){
                int[] cur = queue.poll();
                int r = cur[0], c = cur[1];
                for(int[] d : dirs){
                    int nr = r + d[0];
                    int nc = c + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // rot it
                        fresh--;
                        queue.offer(new int[]{nr, nc});
                        rottedThisMinute = true;
                    }
                }


            }
            if (rottedThisMinute) time++;

        }
        return fresh == 0 ? time : -1; 
        
    }
    
}
