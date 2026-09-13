class Solution:
    def isPalindrome(self, s: str) -> bool:

        #  sanitize string
        s = ''.join(c.lower() for c in s if self.alphaNum(c))
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))