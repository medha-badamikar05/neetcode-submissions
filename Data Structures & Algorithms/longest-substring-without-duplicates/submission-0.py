class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique = set()
        l,r = 0,0
        max_len = 0

        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len