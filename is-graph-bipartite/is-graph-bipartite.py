class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        d = defaultdict(set)
        seen = set()
        A = set()
        B = set()
        
        for i in range(N):
            for node in graph[i]:
                d[i].add(node)
                d[node].add(i)
                
        def go(node):
            nonlocal ans
            if ans:
                for dest in d[node]:
                    if node in A:
                        if dest in A:
                            ans = False
                        else:
                            B.add(dest)
                            if dest not in seen:
                                seen.add(dest)
                                ans = go(dest)
                    else:
                        if dest in B:
                            ans = False
                        else:
                            A.add(dest)
                            if dest not in seen:
                                seen.add(dest)
                                ans = go(dest)
                            
            return ans
        
        for i in range(N):
            ans = True
            if i not in seen:
                A.add(i)
                seen.add(i)
                if not go(i):
                    return False
                
        return True