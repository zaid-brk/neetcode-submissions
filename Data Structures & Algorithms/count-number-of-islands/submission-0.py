class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.traveseid(grid, i, j, r, c)
        
        return count

    def traveseid(self, grid, i, j, r, c):
        if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == '0':
            return 

        grid[i][j] = '0'
        self.traveseid(grid, i, j + 1, r, c)
        self.traveseid(grid, i + 1, j, r, c)
        self.traveseid(grid, i, j - 1, r, c)
        self.traveseid(grid, i - 1, j, r, c)