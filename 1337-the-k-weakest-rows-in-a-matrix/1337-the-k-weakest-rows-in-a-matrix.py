class Solution:
    def kWeakestRows(self, A: List[List[int]], k: int) -> List[int]:
        R, C = len(A), len(A[0])
        #print(list(zip(enumerate(A))))
        tmp = []
        for i, x in enumerate(A):
            tmp.append([i, x])
        tmp.sort(key=lambda x: x[1])
        A = tmp
        return [x[0] for x in A[:k]]