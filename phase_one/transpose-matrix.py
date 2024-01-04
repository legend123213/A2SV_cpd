class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tr_matrix = []
        for i in range(len(matrix[0])):
            ls =[]
            for j in range(len(matrix)):
                ls.append(matrix[j][i])
            tr_matrix.append(ls)
        return tr_matrix
        