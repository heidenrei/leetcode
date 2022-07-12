class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s = sum(nums)
        nums.sort()
        N = len(nums)
        if s % 4:
            return False
        k = s//4
        kset = set()
        for x in range(2**N):
            tmp = 0
            for i in range(N):
                if x & (1<<i):
                    tmp += nums[i]
                    if tmp > k:
                        break
            if tmp == k:
                kset.add(x)
        
        #print(nums)
        kset = list(sorted(list(kset), reverse=True))
        tmp = 0
        rem = 4
        for i in range(min(10, len(kset))):
            tmp = kset[i]
            rem = 3
            #print(kset)
            for x in kset[i+1:]:
                if tmp.bit_count() + x.bit_count() == (tmp | x).bit_count():
                    tmp |= x
                    rem -= 1
                if rem == 0:
                    return True
            
        return False