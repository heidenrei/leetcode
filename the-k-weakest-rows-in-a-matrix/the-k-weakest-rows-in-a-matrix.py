class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = [sum(x) for x in mat]
        
        sums = list(enumerate(sums))
        
        sums.sort(key=lambda x: x[1])
        
        return [x[0] for x in sums[:k]]