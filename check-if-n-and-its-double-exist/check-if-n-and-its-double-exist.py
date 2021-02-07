class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            
            if not arr[i] & 1 and 0 < arr[i]:
                seen.add(arr[i]//2)
            seen.add(arr[i]*2)
            
        return False