class Solution {
public:
    void dfs(int row, int col, vector<vector<char>>& board) {
        if( row < 0 || row == board.size() || col < 0 || col == board[row].size() || board[row][col] != 'O') {
            return;
        }
        board[row][col] = '#';
        dfs(row + 1, col, board);
        dfs(row - 1, col, board);
        dfs(row, col + 1, board);
        dfs(row, col -1, board);
    }

    void solve(vector<vector<char>>& board) {
        for(int i=0;i< board.size();i++) {
            for(int j = 0;j<board[i].size();j++){
                if(board[i][j] == 'O' && (i == 0 || i == board.size()-1) || (j == 0 || j == board[i].size()-1)){
                 dfs(i, j, board);       
                }
            }  
        }

        for(int i=0;i<board.size();i++) {
            for(int j = 0;j<board[i].size();j++){
                if(board[i][j] == 'O'){
                 board[i][j] = 'X';       
                }
            }
            
        }

        for(int i=0;i<board.size();i++) {
            for(int j = 0;j<board[i].size();j++){
                if(board[i][j] == '#'){
                 board[i][j] = 'O';       
                }
            }
            
        }
    }
};
