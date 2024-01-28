class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr_d =[]
        self.ar =[]
        if len(matrix) == 1:
            cop =0
            for h in range(len(matrix[0])):
                self.ar.append(cop+matrix[0][h])
                cop=cop+matrix[0][h]
        else:
            for j in range(len(matrix)):
                co = 0
                res = []
                for i in range(len(matrix[j])):
                    co = co+matrix[j][i]
                    res.append(co)
                self.arr_d.append(res)
            
            self.ar.append(self.arr_d[0])
            for p in range(1, len(matrix)):
                resi = []
                for k in range(len(matrix[p])):
                    resi.append(self.ar[p-1][k] + self.arr_d[p][k])
                self.ar.append(resi)

        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not isinstance(self.ar[0], list):
            if col1 == 0:
                return self.ar[col2]
            else:
                return self.ar[col2] - self.ar[col1 - 1]

        elif row1 == 0 and col1 == 0 and len(self.ar) != 1:
            return self.ar[row2][col2]
        elif row1 == 0:
            return self.ar[row2][col2] - self.ar[row2][col1-1]
        elif col1 == 0:
            return self.ar[row2][col2] - self.ar[row1-1][col2]
        else:
            return self.ar[row2][col2] - self.ar[row1-1][col2] - self.ar[row2][col1-1] + self.ar[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)