class Solution:
    def shiftGrid(self, A: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(A), len(A[0])
        k %= R*C
        d = deque()
        for x in A:
            for y in x:
                d.append(y)
        d.rotate(k)
        A = []
        tmp = []
        while d:
            tmp.append(d.popleft())
            if len(tmp) == C:
                A.append(tmp)
                tmp = []
        return A