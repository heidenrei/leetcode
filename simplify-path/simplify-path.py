class Solution:
    def simplifyPath(self, path: str) -> str:
        path = deque([x for x in path.split('/') if x])
        ans = []
        while path:
            curr = path.popleft()
            if curr == '..':
                if ans:
                    ans.pop()
            elif curr != '.':
                ans.append(curr)
                
        return '/' + '/'.join(ans)