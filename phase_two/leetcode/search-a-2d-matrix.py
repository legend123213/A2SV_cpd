class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t ,b = 0,len(matrix)-1

        while t < b:
            mid = (t+b)//2
            if matrix[mid][-1]>= target:
                b = mid 
            else:
                t = mid +1
        l = 0
        r = len(matrix[0])-1
        while l<r:
            mid = (r+l)//2
            if matrix[t][mid] == target:
                return True
            if matrix[t][mid] > target:
                r = mid
            else:
                l = mid +1
        return False or matrix[t][l] == target
        