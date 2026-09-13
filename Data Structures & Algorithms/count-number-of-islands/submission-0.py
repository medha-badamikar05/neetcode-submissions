class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                paths = [[1,0], [0,1], [-1,0], [0,-1]]
                for pr,pc in paths:
                    if (row + pr) in range(rows) and (col + pc) in range(cols) and grid[row + pr][col + pc] == "1" and ((row + pr), (col + pc)) not in visited:
                        q.append((row+pr, col+pc))
                        visited.add((row+pr, col+pc))
                
               


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
