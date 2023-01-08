class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        N = len(damage)
        
        maxi = max(damage)
        for i in range(N):
            if damage[i] == maxi:
                damage[i] = max(0, damage[i] - armor)
                break
        
        pfs = list(accumulate(damage))
        return max(pfs) + 1
