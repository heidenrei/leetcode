class Solution:
    def findMinStep(self, s: str, hand: str) -> int:
        N = len(s)
        
        @cache
        def compress(s):
            stack = []
            for i, x in enumerate(s):
                stack.append(x)
                if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3] and (i+1 == len(s) or s[i+1] != x):
                    while stack and stack[-1] == x:
                        stack.pop()
            return ''.join(stack)

        
        
        @cache
        def go(s, hand):
            #print(s, hand)
            s = compress(s)
            #print(s, hand)
            #print()
            if not s:
                return 0
            if not hand:
                return inf
            ans = inf
            for j, c in enumerate(hand):
                for i in range(len(s)):
                    if s[i] == c or (i < len(s)-1 and s[i] == s[i+1]):
                        tmp = go(s[:i+1] + c +  s[i+1:], hand[:j] + hand[j+1:]) + 1
                        if tmp < ans:
                            ans = tmp
            return ans
        
        ans = go(s, hand)
        if ans < inf:
            return ans
        else:
            return -1
        