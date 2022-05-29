class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # generate all palindromes then bs
        pals = [x for x in range(0, 10)] + [11]
        N = len(n)
        if N > 1:
            pals.append(int('9'*(N-1)))
            pals.append(pals[-1]+2)
            pals.append(int('9'*N))
            pals.append(pals[-1]+2)
        cand = (int(n[0]) + 1) * 10**(N-1) + int(n[0])+1
        pals.append(cand)
        
        p = N//2
        if N & 1:
            p += 1
            
        for d in range(-1, 2, 1):
            pref = [int(x) for x in n[:p]]
            pref[-1] += d
            if pref[-1] < 0:
                continue
            if N & 1:
                s = pref + pref[:-1][::-1]
            else:
                s = pref + pref[::-1]
            #print(s)
            if len(s) == N:
                #y = ''.join([str(x) for x in s])
                pals.append(int(''.join([str(x) for x in s])))
        pals.sort()
        print(pals)
        best = inf
        besti = None
        n = int(n)
        for i in range(len(pals)):
            if abs(pals[i] - n) < best and pals[i] != n:
                besti = i
                best = abs(pals[i] - n)
        
        return str(pals[besti])
        