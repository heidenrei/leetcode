class Solution:
    def putMarbles(self, weight: List[int], k: int) -> int:
        # we are not given n?
        # it doesnt explicitly say that i ==j is ok

        gaps = []
        for i in range(len(weight)-1):
            gaps.append(weight[i] + weight[i+1])
        gaps.sort()
        mini = sum(gaps[:k-1])
        gaps.reverse()
        maxi = sum(gaps[:k-1])
        return maxi - mini