"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        originalToCloned = {}

        def dfs(n):
            if n in originalToCloned:
                return originalToCloned[n]
            deepCopy = Node(n.val)
            originalToCloned[n] = deepCopy
            for neighbor in n.neighbors:
                deepCopy.neighbors.append(dfs(neighbor))
            return deepCopy
        
        return dfs(node)

        
        
        