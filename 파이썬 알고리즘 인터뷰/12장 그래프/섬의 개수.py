# 나의 풀이 (Runtime: 152ms, Memory: 15.2MB)
class Solution:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        
        for direction in range(4):
            nx = x + self.dx[direction]
            ny = y + self.dy[direction]
            
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == '1':
                    self.dfs(grid, nx, ny)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_island = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    num_of_island += 1
        
        return num_of_island
        

# 책의 풀이 (Runtime: 140ms, Memory: 15.4MB)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 범위를 벗어나거나, 육지가 아닌 경우 종료한다.
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            
            grid[i][j] = '0'
            
            # 동서남북 네 방향에 대해 DFS를 재귀호출한다.
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
