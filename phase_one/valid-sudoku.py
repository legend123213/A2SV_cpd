class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                items = board[i][j]
                if items != ".":
                    res += [(i,items),(items,j),(i//3,j//3,items)]
        return len(res) == len(set(res))
        
