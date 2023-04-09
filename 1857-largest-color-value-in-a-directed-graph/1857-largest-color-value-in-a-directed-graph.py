class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if not edges: return 1 # Edge Case -> no edge -> 1
        n = len(colors) # number of nodes
        roots = {i for i in range(n)} # to check who are root nodes
        graph = defaultdict(set) 
        indegree = defaultdict(int) 
        for a, b in edges:
            graph[a].add(b) # generate graph
            indegree[b] += 1 # save all nodes's indegree
            roots -= {b} # delete nodes who have parent
        
        Max = -1
        # if we use list[] to do dp, we'll use n*26 extra space, and exacly 26 times to update color for all nodes
        # so I decide use double hash to optimize TC & MC
        # dp define as -> max each color count when reach every node
        dp = defaultdict(dict) 
        for root in roots: # search from every root
            indegree[root] = 0 # set root's indegree as 0 (cause indegree hash didn't data for every root)
            dp[root][colors[root]] = 1 # set dp[root]'s color to 1
            q = [root]
            while q: # BFS
                cur = q.pop(0)
                for nxt in graph[cur]:
                    indegree[nxt] -= 1 # update indegree
                    # if we meet a node that indegree == -1, means we found a loop, just return -1
                    # (this situation won't happen when using Topological Sort on a graph without loop)
                    if indegree[nxt] == -1: return -1
                    # update next node's color count
                    for c in dp[cur]:
                        dp[nxt].setdefault(c, dp[cur][c])
                        dp[nxt][c] = max(dp[nxt][c], dp[cur][c])
                    # if we can finally visited next node
                    if indegree[nxt] == 0:
                        q.append(nxt)
                        cc = colors[nxt] # next node's color
                        # add 1 to next node's color count with it's own color
                        dp[nxt].setdefault(cc, 0)
                        dp[nxt][cc] += 1
                        Max = max(Max, dp[nxt][cc]) # update Max
        return Max