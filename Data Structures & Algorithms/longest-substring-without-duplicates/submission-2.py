class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r = 0, 0
        n = len(s)
        maxLen = 0
        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            maxLen = max(maxLen, (r - l + 1))
            r += 1
        return maxLen