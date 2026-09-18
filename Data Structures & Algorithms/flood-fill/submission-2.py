class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
            given an image m x n grid image

            image[i][j] = pixel value of image

            given 3 integers sr, sc, and color

            starting from pixel image[sr][sc]

            begin with the starting pixel and change its color to color

            perform the sam eprocess for each pixel directly adjacent to the original pixel
            process stops when no mroe adjacent pixels of the original color
        '''

        ROWS, COLS = len(image), len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] != orig):
                return 
            #expand in 4 dirs
            image[r][c] = color
            dfs(r + 1,c)
            dfs(r,c + 1)
            dfs(r - 1,c)
            dfs(r,c - 1)
            
        
        dfs(sr, sc)
        return image
            

        