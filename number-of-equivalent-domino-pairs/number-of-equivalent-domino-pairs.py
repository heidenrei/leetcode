class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [tuple(list(sorted(x))) for x in dominoes]
        print(dominoes)
        c = Counter(dominoes)
        ans = 0
        for k, v in c.items():
            v -= 1
            ans += ((v+1)*v)/2
            
        return int(ans)
            