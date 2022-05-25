class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @cache
        def go(b):
            if not b:
                return 0
            N = len(b)
            for i in range(N):
                if b[i] == '1':
                    return (1<<(N-i))-1 - go(b[i+1:])
            return 0
        return go(bin(n)[2:])
    