class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        @cache
        def go(i, cnt):
            if cnt > target:
                return 0
            if i == len(prob):
                return cnt == target
            return round(go(i+1, cnt+1) * prob[i] + go(i+1, cnt) * (1 - prob[i]), 7)
        return go(0, 0)