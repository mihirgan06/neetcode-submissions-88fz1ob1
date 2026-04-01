class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        boolean[][] visited = new boolean[rows][cols];
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    count++;
                    dfs(r, c, grid, visited);
                }
            }
        }

        return count;
    }

    private void dfs(int r, int c, char[][] grid, boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;

        // bounds
        if (r < 0 || r >= rows || c < 0 || c >= cols) return;

        // water or visited
        if (grid[r][c] == '0' || visited[r][c]) return;

        visited[r][c] = true;

        dfs(r + 1, c, grid, visited);
        dfs(r - 1, c, grid, visited);
        dfs(r, c + 1, grid, visited);
        dfs(r, c - 1, grid, visited);
    }
}
