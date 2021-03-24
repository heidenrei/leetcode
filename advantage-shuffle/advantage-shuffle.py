class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        
        A = list(enumerate(A))
        B = list(enumerate(B))
        
        A = [list(x) for x in A]
        B = [list(x) for x in B]           
        
        A = [[x[1], x[0]] for x in A]
        B = [[x[1], x[0]] for x in B]

        
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        A = deque(A)
        B = deque(B)
        
        ans = [None]*N
        tmp = []
        while A and B:
            if A[0][0] > B[0][0]:
                val, _ = A.popleft()
                _, idx = B.popleft()
                ans[idx] = val
            else:
                tmp_b = B.popleft()
                tmp.append(tmp_b)
        
        for _, idx in tmp:
            val, _ = A.popleft()
            ans[idx] = val
        
        return ans