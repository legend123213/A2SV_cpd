class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board),len(board[0])
        k = set()
        def backTracking(i,j,ptr):
            if ptr == len(word):
                return True
            if i>=row or j >=col or i<0 or j < 0 or ptr>len(word)  or word[ptr]!=board[i][j] or (i,j) in k:
                return False
            
            k.add((i,j))
            res = backTracking(i+1,j,ptr+1) or backTracking(i-1,j,ptr+1) or backTracking(i,j+1,ptr+1) or backTracking(i,j-1,ptr+1)
            k.remove((i,j))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backTracking(r,c,0):
                    return True
        return False
            
           
        