class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        for x in s:
            if x == '#':
                if stacks:
                    stacks.pop()
            else:
                stacks.append(x)
                
        for x in t:
            if x == '#':
                if stackt:
                    stackt.pop()
            else:
                stackt.append(x)
                
        return stackt == stacks