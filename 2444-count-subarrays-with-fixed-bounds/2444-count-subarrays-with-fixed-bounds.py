class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        groups = []
        for k in groupby(nums, key=lambda x: minK <= x <= maxK):
            if k[0]:
                groups.append(list(k[1]))
        
        def bc(x):
            return (x*(x+1))//2
        
        def count(group):
            if minK not in group or maxK not in group:
                return 0
            N = len(group)
            
            if minK == maxK:
                return bc(N)
            ans = 0
            leftmax = [-1]
            leftmin = [-1]
            for i in range(N):
                if group[i] == minK:
                    leftmin.append(i)
                else:
                    leftmin.append(leftmin[-1])
                if group[i] == maxK:
                    leftmax.append(i)
                else:
                    leftmax.append(leftmax[-1])
            
            rightmax = [N]
            rightmin = [N]
            for i in range(N-1, -1, -1):
                if group[i] == minK:
                    rightmin.append(i)
                else:
                    rightmin.append(rightmin[-1])
                if group[i] == maxK:
                    rightmax.append(i)
                else:
                    rightmax.append(rightmax[-1])
            
            rightmax.reverse(); rightmin.reverse()

            for i in range(N):
                if group[i] == minK:
                    tmp = 0
                    lmi = leftmin[i] # subarrays with next minK to the left are already counted
                    lma = leftmax[i]
                    rma = rightmax[i]
                    to_add = (i-lmi)*(N-i)
                    to_sub = (rma-i)*(i-max(lma, lmi))
                    tmp += to_add - to_sub
                    ans += tmp
                    
            return ans
        ans = 0
        for group in groups:
            ans += count(group)
        return ans