class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        curr = s[0]
        run = 1
        i = 1
        N = len(s)
        stack = []
        while i < N:
            if s[i] == curr:
                run += 1
            else:
                multi = run
                if stack and stack[-1][0] == curr:
                    x = stack.pop()
                    multi += x[1]
                multi %= k
                if multi:
                    stack.append([curr, multi])
                curr = s[i]
                run = 1
            i += 1
        multi = run
        if stack and stack[-1][0] == curr:
            x = stack.pop()
            multi += x[1]
        multi %= k
        if multi:
            stack.append([curr, multi])
                
        ans = ''
        for x, y in stack:
            ans += x*y
        return ans
        