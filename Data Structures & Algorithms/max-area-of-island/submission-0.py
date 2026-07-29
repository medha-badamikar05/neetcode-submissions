class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
            
    
        for i in range(R):
            for j in range(C):
                maxArea = max(maxArea, dfs(i,j))
        return maxArea
        