class Solution:
    def lastRemaining(self, n):
        
        # keep track of the first number in the next array
        first=1
        distance=1
        step=0
        while n>1:
            if step%2==0 or n%2!=0:
                first+=distance
            distance=distance<<1
            step+=1
            n=n>>1
        return first