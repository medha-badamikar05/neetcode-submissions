class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap = {}

        if len(s) != len(t):
            return False
        
        for a,b in zip(s,t):
            countMap[a] = countMap.get(a, 0) + 1
            countMap[b] = countMap.get(b, 0) - 1
        
        
        return all(v == 0 for v in countMap.values())
