class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for i in range(len(mat)):
            summ+=mat[i][i]
            summ+=mat[i][len(mat)-1-i]
        return summ-mat[len(mat)//2][len(mat)//2] if len(mat)%2!=0 else summ


        