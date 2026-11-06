class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n,m = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if (row+dr) < n and (row+dr) >= 0 and (col+dc) < m and (col+dc) >=0 and grid[row+dr][col+dc] == "1" and (row+dr,col+dc) not in visited:
                        q.append((row+dr, col+dc))
                        visited.add((row+dr,col+dc))
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
