class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        summ = 0
        for i in range(len(grid)):
            prefix_sum = 0
            for j in range(len(grid[0])):
                grid[i][j]+=prefix_sum
                prefix_sum = grid[i][j] 
        for i in grid:
            i.insert(0,0)
        print(grid)
        max_res = 0
        for row in range((len(grid)-3)+1):
            for col in range(3,len(grid[0])):
                sum_of_grid = (grid[row][col]-grid[row][col-3]) + (grid[row+1][col-1]-grid[row+1][col-2]) + (grid[row+2][col]-grid[row+2][col-3])
                max_res = max(max_res,sum_of_grid)
        return max_res
