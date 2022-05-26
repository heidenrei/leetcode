class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        M = len(key)
        
        @cache
        def go(i, j):
            if j == M:
                return 0
            ni = i
            move_right = 0
            while ring[ni] != key[j]:
                ni += 1
                ni %= N
                move_right += 1
            
            right = go(ni, j+1) + move_right + 1
            
            nii = i
            move_left = 0
            while ring[nii] != key[j]:
                nii -= 1
                if nii == -1:
                    nii = N - 1
                move_left += 1
            left = go(nii, j+1) + move_left + 1
            return min(left, right)
        
        return go(0, 0)