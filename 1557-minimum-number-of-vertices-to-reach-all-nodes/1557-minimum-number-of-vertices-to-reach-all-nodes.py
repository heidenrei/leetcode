class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seen = set()
        d = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in edges:
            d[x].append(y)
            indegree[y] += 1
        
        ans = set()
        for x in range(n):
            if x not in indegree:
                ans.add(x)
        return sorted(list(ans))
        