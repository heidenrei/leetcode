from sortedcontainers import SortedList

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        A = []
        for i in range(N):
            tmp = []
            for j in range(i+1, N):
                tmp.append(arr[i]/arr[j])
            if tmp:
                A.append(tmp[::-1])
        
        q = SortedList()
        q.add([A[0][0], tuple([0, 0])])
        
        cnt = 0
        ans = None
        seen = set()
                
        while cnt < k:
            v, x = q.pop(0)
            i, j = x
            
            cnt += 1
            ans = [arr[i], arr[N-j-1]]
            tmpr = math.inf
            tmpl = math.inf
            
            if j + 1 < N-i-1 and tuple([i, j+1]) not in seen:
                #tmpr = A[i][j+1]
                seen.add(tuple([i, j+1]))
                q.add([A[i][j+1], tuple([i, j+1])])
            if i + 1 < N-j-1 and tuple([i+1, j]) not in seen:
                #tmpl = A[i+1][j]
                seen.add(tuple([i+1, j]))
                q.add([A[i+1][j], tuple([i+1, j])])
                
            # if tmpr < tmpl:
            #     if tmpr != math.inf:
            #         seen.add(tuple([i, j+1]))
            #         q.add([A[i][j+1], tuple([i, j+1])])
            # else:
            #     if tmpl != math.inf:
            #         seen.add(tuple([i+1, j]))
            #         q.add([A[i+1][j], tuple([i+1, j])])
        
        return ans