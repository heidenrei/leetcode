class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:        
        bits.reverse()
        
        cnt = 0
        
        for i in range(1, len(bits)):
            if bits[i] == 1:
                cnt += 1
            else:
                break
        
        if cnt % 2 == 1:
            return False
        else:
            return True
                