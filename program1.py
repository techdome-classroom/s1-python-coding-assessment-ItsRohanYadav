class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        rows, cols =len(grid), len(grid[0])
        total_isles=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    total_isles += 1
                    dfs(i, j)
                    if r<0 or r>=rows or c<0 or c>=cols or grid[i][j]=='W':
                        

        
                    
        return 0 
