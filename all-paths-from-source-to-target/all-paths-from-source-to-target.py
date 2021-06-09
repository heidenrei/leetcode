class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []
        
        def go(path):
            for child in graph[path[-1]]:
                if child not in path:
                    if child == N - 1:
                        ans.append(list(path) + [child])
                    else:
                        tmp = list(path)
                        tmp.append(child)
                        go(tuple(tmp))
                        
        go(tuple([0]))
        return ans