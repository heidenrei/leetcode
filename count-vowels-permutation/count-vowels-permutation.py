class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def go(i, rem):
            ans = 0

            if rem == 0:
                return 1
            if i == 0:
                if rem - 1 > 0:
                    ans = go(1, rem-1)
                else:
                    return 1
            elif i == 1:
                if rem - 1 > 0:
                    ans += go(0, rem-1)
                    ans += go(2, rem-1)
                else:
                    return 2
            elif i == 2:
                if rem - 1 > 0:
                    ans += go(0, rem-1)
                    ans += go(1, rem-1)
                    ans += go(3, rem-1)
                    ans += go(4, rem-1)
                else:
                    return 4
            elif i == 3:
                if rem - 1 > 0:
                    ans += go(2, rem-1)
                    ans += go(4, rem-1)
                else:
                    return 2
            else:
                if rem - 1 > 0:
                    ans = go(0, rem-1)
                else:
                    return 1
                    
            
            return ans
            
        return sum([go(x, n-1) for x in range(5)]) % (10**9+7)