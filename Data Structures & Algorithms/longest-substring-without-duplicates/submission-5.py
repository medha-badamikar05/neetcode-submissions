class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        n = len(s)
        longestSubstring = 0
        l,r = 0,0

        while r < n:
            while s[r] in unique:
                unique.remove(s[l])   
                l += 1
            unique.add(s[r])
            longestSubstring = max(longestSubstring, len(unique))
            r += 1
        return longestSubstring
        