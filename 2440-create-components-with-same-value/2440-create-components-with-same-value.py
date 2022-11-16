class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return 0
        s = sum(nums)
        N = len(nums)
        
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
            
        leaves = set()
        for key in d:
            if len(d[key]) == 1:
                leaves.add(key)
        leaves = list(leaves)
        # print(leaves)
        ans = 1
        def is_good(k):
            #dfs in from all the leaves and check that all nodes are in seen
            ans = True
            def dfs(node, prev):
                rem = 0
                for nei in d[node]:
                    if nei != prev:
                        tmp = dfs(nei, node)
                        if tmp == k:
                            tmp = 0
                        rem += tmp
                if rem + nums[node] > k:
                    nonlocal ans
                    ans = False
                if rem + nums[node] == k:
                    return 0
                else:  
                    return rem + nums[node]
            if leaves:
                if dfs(leaves[0], None) % k:
                    #nonlocal ans
                    ans = False
            return ans
        
        divs = set()
        
        for k in range(1, ceil(sqrt(s))+1):
            if not s%k:
                divs.add(k)
                divs.add(s//k)
        # is_good(6)
        # return
        for k in divs:
            # print(k)
            if is_good(k):
                if s//k > ans:
                    ans = s//k
                    
        return ans - 1