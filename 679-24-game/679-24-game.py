class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        ops = ['+', '-', '*', '/']
        @cache
        def go(A):
            # if len(A) == 1:
            #     print(A)
            N = len(A)
            if N == 1 and round(A[0], 5) == 24:
                return True
            for p in permutations(A):
                for i in range(1, N):
                    for op in ops:
                        left, right = p[i-1], p[i]
                        if op != '/' or right != 0:
                            if go(tuple(list(p[:i-1]) + [eval(str(left) + op + str(right))] + list(p[i+1:]))):
                                return True
            return False
        
        return go(tuple(cards))