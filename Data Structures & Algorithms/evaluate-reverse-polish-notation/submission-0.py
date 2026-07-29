class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        add = "+"
        sub = "-"
        prd = "*"
        div = "/"

        stack = []
        
        for c in tokens:
            if c == add:
                stack.append(stack.pop() + stack.pop())
            elif c == sub:
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == prd:
                stack.append(stack.pop() * stack.pop())
            elif c == div:
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        
        return stack.pop()