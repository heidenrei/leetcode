class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = {'[': ']', '{': '}', '(': ')'}
        for bracket in s:
            if bracket in openers:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if bracket != openers[last]:
                    return False
                
        return not stack
