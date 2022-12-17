class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                a,b = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                elif i == "/":
                    # int() would automatically round to 0
                    stack.append(int(b / a))
        return stack.pop()