class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        d = defaultdict(list)
        
        for i in range(N):
            accounts[i] = [accounts[i][0], set(accounts[i][1:])]
        
        for i in range(N):
            for j in range(i):
                if accounts[i][0] == accounts[j][0] and len(accounts[i][1] | accounts[j][1]) < len(accounts[i][1]) + len(accounts[j][1]):
                    d[i].append(j)
                    d[j].append(i)
                    
        parent = [x for x in range(N)]
        
        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            parent[ux] = uy
                
        for i in range(N):
            for j in d[i]:
                if ufind(j) != ufind(i):
                    uunion(j, i)                
        
        set_list = [set() for x in range(N)]
        
        for i in range(N):
            set_list[ufind(i)] |= accounts[i][1]
            
        ans = []
        
        
        for i in range(N):
            if set_list[i]:
                ans.append([accounts[i][0]] + sorted([x for x in set_list[i]]))
                
        return ans