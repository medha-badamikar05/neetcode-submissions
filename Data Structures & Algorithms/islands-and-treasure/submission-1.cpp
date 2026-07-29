class Solution {
public:
    void traverse(int i, int j, vector<vector<int>>& grid, vector<vector<int>>& visited, queue<pair<int, int>>& bfs) {
        int n = grid.size(), m = grid[0].size();
        if (i < 0 || j < 0 || i >= n || j >= m) return;     
        if (visited[i][j] || grid[i][j] == -1) return;       

        visited[i][j] = 1;
        bfs.push({i, j});
    }

    void islandsAndTreasure(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        queue<pair<int, int>> bfs;
        vector<vector<int>> visited(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    visited[i][j] = 1;
                    bfs.push({i, j});
                }
            }
        }

        int level = 0;
        while (!bfs.empty()) {
            int sz = bfs.size();
            for (int x = 0; x < sz; x++) {
                auto [i, j] = bfs.front();
                bfs.pop();

                grid[i][j] = level;

                traverse(i + 1, j, grid, visited, bfs);
                traverse(i - 1, j, grid, visited, bfs);
                traverse(i, j + 1, grid, visited, bfs);
                traverse(i, j - 1, grid, visited, bfs);
            }
            level++;
        }
    }
};
