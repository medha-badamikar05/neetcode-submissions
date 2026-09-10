class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueElements = set()
        l,r = 0,0
        longestSubstring = 0
        n = len(s)
        
        while r < n:
            while uniqueElements and s[r] in uniqueElements:
                uniqueElements.remove(s[l])
                l += 1
            uniqueElements.add(s[r])
            longestSubstring = max(longestSubstring, (r-l+1))
            r += 1
        return longestSubstring