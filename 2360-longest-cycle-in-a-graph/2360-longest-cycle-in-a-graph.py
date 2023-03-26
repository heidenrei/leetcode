class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def find_SCC(graph):
            SCC, S, P = [], [], []
            depth = [0] * len(graph)

            stack = list(range(len(graph)))
            while stack:
                node = stack.pop()
                if node < 0:
                    d = depth[~node] - 1
                    if P[-1] > d:
                        SCC.append(S[d:])
                        del S[d:], P[-1]
                        for node in SCC[-1]:
                            depth[node] = -1
                elif depth[node] > 0:
                    while P[-1] > depth[node]:
                        P.pop()
                elif depth[node] == 0:
                    S.append(node)
                    P.append(len(S))
                    depth[node] = len(S)
                    stack.append(~node)
                    #print(stack, graph, node)
                    if graph[node] != -1:
                        stack.append(graph[node])
            return SCC[::-1]
        
        sccs = find_SCC(edges)
        ans = len(max(sccs, key=len))
        return ans if ans > 1 else -1