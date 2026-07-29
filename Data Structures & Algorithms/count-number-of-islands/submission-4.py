class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        islands = 0
        visitedLands = set()


        def bfs(r, c):
           
            def checkNeighbour(r, c):
                if r < 0 or c < 0 or r == R or c == C or grid[r][c] == "0" or (r,c) in visitedLands:
                    return
                bfs_q.append((r,c))
                visitedLands.add((r,c))

            bfs_q = deque()
            bfs_q.append((r,c))
            visitedLands.add((r,c))
            while bfs_q:
                r,c = bfs_q.popleft()
                checkNeighbour(r, c+1)
                checkNeighbour(r, c-1)
                checkNeighbour(r + 1, c)
                checkNeighbour(r - 1, c)
            

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visitedLands:
                    bfs(i,j)
                    islands += 1
        return islands

        
            



            
