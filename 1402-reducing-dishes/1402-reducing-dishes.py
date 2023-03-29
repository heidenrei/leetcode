import cmath

MOD = 10**9 + 7


def fft(a, inv=False):
    n = len(a)
    w = [cmath.rect(1, (-2 if inv else 2) * cmath.pi * i / n) for i in range(n >> 1)]
    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= n >> 1
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    step = 2
    while step <= n:
        half, diff = step >> 1, n // step
        for i in range(0, n, step):
            pw = 0
            for j in range(i, i + half):
                v = a[j + half] * w[pw]
                a[j + half] = a[j] - v
                a[j] += v
                pw += diff
        step <<= 1

    if inv:
        for i in range(n):
            a[i] /= n


def fft_conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a.extend([0.0] * (n - len(a)))
    b.extend([0.0] * (n - len(b)))

    fft(a), fft(b)
    for i in range(n):
        a[i] *= b[i]
    fft(a, True)

    a = [a[i].real for i in range(s)]
    return [round(x) for x in a]

class Solution:
    def maxSatisfaction(self, nums):
        nums.sort(reverse=True)
        n = len(nums)
        if n == 1:
            return max(0, nums[0])
        def get_score(i):
            a = nums[:i]
            b = indices[:i]
            a += [0]*i
            b += b
            c = fft_conv(a, b)
            #print(c)
            #print(i-1)
            tmp = c[i-1]
            return tmp
        def is_increasing(i):
            return get_score(i+1) > get_score(i)
        
        
        indices = [x+1 for x in range(n)]
        
        l, r = 1, len(nums)-2
        while l < r:
            m = l + (r-l+1)//2
            if is_increasing(m):
                l = m
            else:
                r = m - 1
        l, m, r = get_score(1), get_score(r+1), get_score(len(nums))
        return max(l, m , r, 0)        

        return best