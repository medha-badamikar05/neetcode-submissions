class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        longestSub = 0
        unique = set()
         
        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right]) 
            longestSub = max(longestSub, right - left + 1)
            right += 1
            
        return longestSub