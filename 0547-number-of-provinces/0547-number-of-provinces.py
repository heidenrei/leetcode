class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        ans = 0
        N = len(A)
        seen = set()
        def dfs(node):
            seen.add(node)
            for child in d[node]:
                if child not in seen:
                    dfs(child)
                    
        d = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if A[i][j]:
                    d[i].append(j)
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
                
        return ans