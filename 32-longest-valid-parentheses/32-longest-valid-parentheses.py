class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        best = 0
        
        for open_char, iterator in [("(", range(n)), (")", reversed(range(n)))]:
            open_count = close_count = 0
            for i in iterator:
                if s[i] == open_char:
                    open_count += 1
                elif open_count == close_count:
                    open_count = close_count = 0
                else:
                    close_count += 1
                    if open_count == close_count:
                        best = max(best, open_count * 2)
        
        return best