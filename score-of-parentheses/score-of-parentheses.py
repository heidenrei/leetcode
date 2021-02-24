class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        N = len(s)
        cnt = 0
        for i in range(N):
            if s[i] == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                    continue
                    
                curr = 0
                while stack[-1] != '(':
                    tmp = stack.pop()
                    if isinstance(tmp, int):
                        curr += tmp
                
                stack.pop()
                stack.append(curr*2)
                
        return sum(stack)