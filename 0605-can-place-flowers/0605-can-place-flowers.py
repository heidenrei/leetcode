class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        rem = n
        for i in range(len(a)):
            #p#rint(i, (i == 0 or not a[i-1]), (i == len(a)-1 or not a[i+1]))
            if not a[i] and (i == 0 or a[i-1] != 1) and (i == len(a)-1 or a[i+1] != 1):
                a[i] = 1
                rem -= 1
        #print(a)
        return rem <= 0