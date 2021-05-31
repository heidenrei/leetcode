class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        N = len(arr)
        
        arr.sort()
        
        diff = arr[0] - arr[1]
        
        for i in range(1, N-1):
            if arr[i] - arr[i+1] != diff:
                return False
            
        return True