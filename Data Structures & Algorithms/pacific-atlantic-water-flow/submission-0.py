class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited, prevHeight):
            if i < 0 or j < 0 or i == rows or j == cols or (i,j) in visited or heights[i][j] < prevHeight:
                return 
            visited.add((i,j))
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0]) # res -> i,j
            dfs(i, cols-1, atlantic, heights[i][cols-1])
        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows - 1, j, atlantic, heights[rows-1][j])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
