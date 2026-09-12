# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialStr = []
        def dfs(node):
            if not node:
                serialStr.append("n")
                return
            serialStr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
          
        dfs(root)
        print("serialized output: ", serialStr)
        return ",".join(serialStr)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        attrs = data.split(",")
        self.i = 0

        def dfs():
            if attrs[self.i] == "n":
                self.i += 1
                return None
            node = TreeNode(val = attrs[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
