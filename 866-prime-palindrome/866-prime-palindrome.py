class Solution:
    def primePalindrome(self, n: int) -> int:
        
        def is_prime(x):
            if x == 2:
                return True
            x = int(x)
            for d in range(2, ceil(sqrt(x))+1):
                if x/d % 1 == 0:
                    return False
            return True
        
        pals = [x for x in range(2, 10) if is_prime(x)]
        pals.append(11)
        if n <= 11:
            return pals[bisect_left(pals, n)]
        
        for x in range(1, 10**3+1):
            pre = str(x)
            suf = str(x)[::-1]
            num = int(pre+suf)
            if num >= n and is_prime(num):
                return num
            #pals.append(pre+suf)
            for y in range(10):
                num = int(pre + str(y) + suf)
                if num >= n and is_prime(num):
                    return num
                #pals.append(pre + str(y) + suf)
        #print(pals)
        #pals = [int(x) for x in pals if is_prime(x)]
        #print(pals)
        #return pals[bisect_left(pals, n)]