import bisect
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        local_cnt = 0
        global_cnt = 0
        seen = []
        for i in range(N):
            num_bigger = len(seen) - bisect.bisect_right(seen, A[i])
            global_cnt += num_bigger
            bisect.insort(seen, A[i])
            if i + 1 < N:
                local_cnt += A[i] > A[i+1]

        return local_cnt == global_cnt