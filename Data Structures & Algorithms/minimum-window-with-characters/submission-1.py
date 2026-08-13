class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        subStringMap = {}
        windowMap = {}
        l,r = 0,0
        n = len(s)
        res, resLen = [-1,-1], float("infinity")

        for c in t:
            subStringMap[c] = subStringMap.get(c,0) + 1
        cur = 0
        req = len(subStringMap)

        while r < n:
            windowMap[s[r]] = windowMap.get(s[r],0) + 1
            if s[r] in subStringMap and windowMap[s[r]] == subStringMap[s[r]]:
                cur += 1
            while cur == req:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                windowMap[s[l]] -= 1
                if s[l] in subStringMap and windowMap[s[l]] < subStringMap[s[l]]:
                    cur -= 1
                l += 1
            r += 1
        
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""