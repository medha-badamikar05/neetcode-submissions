class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False
        
        stack = []
        for p in s:
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            if p == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            if p == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if p == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 