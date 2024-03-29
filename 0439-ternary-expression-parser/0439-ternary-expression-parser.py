class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for c in reversed(expression):
            stack.append(c)
            if stack[-2:-1] == ['?']:
                stack[-5:] = stack[-3 if stack[-1] == 'T' else -5]
        return stack[0]