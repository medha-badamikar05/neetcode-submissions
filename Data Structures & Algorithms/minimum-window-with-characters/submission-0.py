class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1

        res = ""
        required = len(countT)
        current = 0
        countS = defaultdict(int)

        n = len(s)
        l, r = 0, 0
        while r < n:
            c = s[r]
            countS[c] += 1
            if c in countT and countS[c] == countT[c]:
                current += 1

            while l<= r and required == current:
                if res == "" or (r-l+1) < len(res):
                    res = s[l:r+1]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    current -= 1
                l += 1
            r += 1
        return res
        
