from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        self.digraph = defaultdict(set)
        self.dp = [0]*numCourses
        
        for c, p in prerequisites:
            self.digraph[p].add(c)
            
        for i in range(numCourses):
            if self.dp[i] == 0 and not self.dfs(i):
                return False
        return True
    
    def dfs(self, x):
        self.dp[x] = -1
        for c in self.digraph[x]:
            if self.dp[c] == -1:
                return False
            if self.dp[c] == 0 and not self.dfs(c):
                return False
        self.dp[x] = 1
        return True