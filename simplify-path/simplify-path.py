class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        def f(el):
            if not el:
                return False
            elif el == '.':
                return False
            else:
                return True
            
        path = list(filter(f, path))
        
        stack = []
        
        idx = 0
        
        while idx < len(path):
            if path[idx] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[idx])
                
            idx += 1
        
        return '/' + '/'.join(stack)
