class Solution {
    /**
    Given an image represented by mxn grid of integers image, where image[i][j] is a pixel value of image
    sr, sc, and color, task is to perform a flood fill on the image starting from image[sr][sc]

    Begin with the starting pixel and change its color to color
    Perform the same process for every pixel direcrly adjacent
    Keep repeating this process by checking neighboring pixels and modifying the color
    Process stpps when no more adjacent color to update
    */
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        if(original == color) return image;

        int rows = image.length;
        int cols = image[0].length;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{sr,sc});
        image[sr][sc] = color;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        while(!q.isEmpty()){
            int[] cell = q.poll();
            int r = cell[0], c = cell[1];
            for(int[] d : dirs){
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {

                    // check if this cell needs to be filled
                    if (image[nr][nc] == original) {
                        image[nr][nc] = color;
                        q.offer(new int[]{nr, nc});
                    }
                }
            }

        }
        return image;
        
    }
}