class Solution:
    def minOperations(self, n: int) -> int:
        A = []
        for i in range(n):
            A.append((2*i)+1)
        ans = 0
        target = n//2
        for i in range(n):
            ans += abs(A[i] - A[target])

        return ans // 2