class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = deque()
        times, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    visited.append([r,c])
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while visited and fresh > 0:
            for i in range(len(visited)):
                r,c = visited.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if(row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                
                    grid[row][col] = 2
                    visited.append([row,col])
                    fresh -= 1
            times += 1


        return times if fresh == 0 else -1



