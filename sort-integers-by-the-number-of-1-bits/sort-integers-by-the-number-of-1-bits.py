class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = list(zip(arr, [sum([int(y) for y in bin(x)[2:]]) for x in arr]))
        ans.sort(key=lambda x: [x[1], x[0]])
        
        return [x[0] for x in ans]
