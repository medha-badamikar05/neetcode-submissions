class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charSortForS = frozenset(Counter(s).items())
        charSortForT = frozenset(Counter(t).items())

        if charSortForS == charSortForT:
            return True
        return False