class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def go(s):
            if len(s) == n*2:
                ans.append(s)
                return
            else:
                go(s+')')
                go(s+'(')
        
        go('(')
                
        def is_valid(s):
            openb = 0
            for b in s:
                if b == ')':
                    if openb > 0:
                        openb -= 1
                    else:
                        return False
                else:
                    openb += 1
                    
            return openb == 0
                
        ans = [x for x in ans if is_valid(x)]
        
        return ans