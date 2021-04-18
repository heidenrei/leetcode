class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        N1, N2 = len(arr1), len(arr2)
        xor1, xor2 = 0, 0
        for i in range(N1):
            xor1 ^= arr1[i]
            
        for i in range(N2):
            xor2 ^= arr2[i]
                
        return xor1 & xor2 