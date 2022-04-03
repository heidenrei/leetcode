class Solution:
    def stoneGameVI(self, astones: List[int], bstones: List[int]) -> int:
        N = len(astones)
        stones = [[astones[i]+bstones[i], i] for i in range(N)]
        stones.sort(key=lambda x: -abs(x[0]))
        #print(stones)
        a = 0
        b = 0
        for idx, [_, i] in enumerate(stones):
            if not idx & 1:
                a += astones[i]
            else:
                b += bstones[i]
                
        if a > b:
            return 1
        elif b > a:
            return -1
        else:
            return 0