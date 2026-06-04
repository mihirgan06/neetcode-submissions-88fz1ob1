class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
            Given a 2D grid of characters board, and string word return true of the word is present in grid else fasle

            go horizontal or vertical based on the word

            So say we have this as the word - CAT
            board = [
                ["A","B","C","D"],
                ["S","A","A","T"],
                ["A","C","A","E"]
            ],
                word = "CAT"
            we can start at left corner and recurse in 4 directions, until we find C, and then again continue but we wil eventually find it with some path


        '''

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            #rows, cols, and index of the word
            #r,c can represent the cell we are at rn
            

            if i == len(word):
                return True #we found the full word
            if (
                r < 0 or 
                c < 0 or 
                r == ROWS or 
                c == COLS or 
                (r, c) in visited
                or board[r][c] != word[i]
            ):
                return False
            
            visited.add((r,c))
            #increment i within the recursive calls as once we add one letter we look for the next
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return found
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False