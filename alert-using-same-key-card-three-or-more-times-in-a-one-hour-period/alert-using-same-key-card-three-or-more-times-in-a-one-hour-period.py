class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def get_time(s):
            time = 0
            time += int(s[:2])*60
            time += int(s[3:])
            return time
        
        N = len(keyName)
        cnts = defaultdict(int)
        d = deque()
        ans = set()
        
        keyTime = [get_time(x) for x in keyTime]
        
        A = list(zip(keyTime, keyName))
        A.sort()
        
        for i in range(N):
            #first clear d for all entries < curr time
            while d and d[0][0] < A[i][0]:
                cnts[d.popleft()[1]] -= 1
                
            d.append([A[i][0]+60, A[i][1]])
            cnts[A[i][1]] += 1
            if cnts[A[i][1]] >= 3:
                ans.add(A[i][1])
                
        return sorted(list(ans))
                
                