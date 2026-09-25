class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
    
        countT, countS = {}, {}

        for c in t:
            countT[c] = countT.get(c,0) + 1
        
        req = len(countT)
        cur = 0
        l, r = 0, 0
        resLen, resL = float("inf"), 0
        n = len(s)

        while r < n:
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                cur += 1
            while req == cur:
                if r - l + 1 < resLen:
                    resLen, resL = r - l + 1, l
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    cur -= 1
                l += 1
            r += 1
        return s[resL: resL + resLen] if resLen != float("inf") else ""
        

