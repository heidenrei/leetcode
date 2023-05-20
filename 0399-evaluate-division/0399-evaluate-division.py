class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        names = dict()
        index = 0
        for x, y in equations:
            if x not in names:
                names[x] = index
                index += 1
            if y not in names:
                names[y] = index
                index += 1
                
        N = len(names)
        g = [[None]*N for _ in range(N)]
        
        for index, (x, y) in enumerate(equations):
            g[names[x]][names[y]]= values[index]
            g[names[y]][names[x]] = 1.0 / values[index]
            
            
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if g[i][j] is None and g[i][k] is not None and g[k][j] is not None:
                        g[i][j] = g[i][k] * g[k][j]
                        
        results = []
        for x, y in queries:
            if x not in names or y not in names:
                results.append(-1)
                continue
            if g[names[x]][names[y]] is not None:
                results.append(g[names[x]][names[y]])
            else:
                results.append(-1)
        return results