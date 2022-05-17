class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        snum = str(num)
        N = len(snum)
        for i in range(N-k+1):
            intd = int(snum[i:i+k])
            ans += intd and num % intd == 0
            
        return ans