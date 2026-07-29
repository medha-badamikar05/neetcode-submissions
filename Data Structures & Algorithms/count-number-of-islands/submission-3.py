class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):

            def checkNeighbor(p, q):
                if p < 0 or q < 0 or p == R or q == C or (p,q) in visited or grid[p][q] == "0":
                    return
                bfsQueue.append((p,q))
                visited.add((p,q))

            bfsQueue = deque()
            bfsQueue.append((r,c))
            visited.add((r,c))

            while bfsQueue:
                p, q = bfsQueue.popleft()
                checkNeighbor(p + 1, q)
                checkNeighbor(p - 1, q)
                checkNeighbor(p, q + 1)
                checkNeighbor(p, q - 1)      

        # check islands
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
        