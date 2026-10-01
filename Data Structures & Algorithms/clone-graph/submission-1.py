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
        originalToClone = {}

        def dfs(node):
            if node in originalToClone:
                return originalToClone[node]
            cloneNode = Node(val = node.val)
            originalToClone[node] = cloneNode
            for i in node.neighbors:
                cloneNode.neighbors.append(dfs(i))
            return cloneNode 
        return dfs(node)
       
        
        
        