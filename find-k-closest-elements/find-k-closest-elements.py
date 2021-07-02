class Solution:
    def findClosestElements(self, arr: List[int], k: int, t: int) -> List[int]:
        arr.sort(key=lambda x: (abs(t-x), x))
        return sorted(arr[:k])