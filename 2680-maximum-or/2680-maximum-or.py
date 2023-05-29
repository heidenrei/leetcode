class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        
        #print(bin(94)[2:].zfill(8))
        #print(bin(35)[2:].zfill(8))
        #print((94<<k) | 35)
        for x in nums:
            ans |= x
            for i in range(32):
                if x & (1<<i):
                    d[i] += 1
        best = 0            
        for x in nums:
            tmp = ans# | (x<<k)
            #print(x<<k, tmp)
            for i in range(32):
                if x & (1<<i) and d[i] == 1:
                    #print(i)
                    tmp ^= 1<<i
            tmp |= (x<<k)
            
            if tmp > best:
                best = tmp
        return best