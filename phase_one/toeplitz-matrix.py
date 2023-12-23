class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n,m=len(matrix),len(matrix[0])
        for i in range(len(matrix[0])):
            k = i
            l = 0
            tester = matrix[0][i]
            while l<n and k<m:
                print(l,k)
                if tester!=matrix[l][k]:
                    return False
                k+=1
                l+=1
        for j in range(len(matrix)):
            k = j
            l = 0
            tester = matrix[j][0]
            while l<m and k<n:
                print(k,l)
                if tester!=matrix[k][l]:
                    return False
                k+=1
                l+=1
        
        return True
