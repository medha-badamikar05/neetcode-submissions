class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            charMatch = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or charMatch and dfs(i+1, j)
            if charMatch:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)