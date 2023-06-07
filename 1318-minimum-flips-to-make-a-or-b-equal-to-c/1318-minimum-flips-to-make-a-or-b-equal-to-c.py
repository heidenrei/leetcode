class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            ab, bb, cb = a & (1<<i), b & (1<<i), c & (1<<i)
            if cb:
                if ab | bb:
                    continue
                else:
                    ans += 1
            else:
                if ab & bb:
                    ans += 2
                elif ab | bb:
                    ans += 1
                else:
                    continue
        return ans
                        
            