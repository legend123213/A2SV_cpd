class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid[0])):
            grid[1][i]=grid[1][i]+grid[1][i-1]
        ls = grid[0][::-1]
        for j in range(1,len(ls)):
            ls[j]=ls[j]+ls[j-1]
        grid[0]=ls[::-1]
        mac = 0
        ind = 0
        if len(grid[0])==1:
            return 0
        while ind<len(grid[0]):
            if ind == 0:
                mac = grid[0][ind+1]
                pass
            if ind == len(grid[0])-1:
                mac = min(mac,grid[1][ind-1])
            else:
                max_interval = max(grid[0][ind+1],grid[1][ind-1])
                mac = min(mac,max_interval)
            ind+=1
        return mac

        