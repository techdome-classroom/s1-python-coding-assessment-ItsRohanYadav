class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        rows, cols =len(grid), len(grid[0])
        total_isles=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    total_isles += 1
                    if i<0 or i>= rows or j<0 or j>= cols or grid[i][j]
        
                    
        return 0 
