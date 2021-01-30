class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        N = len(arr)
        
        A = list(accumulate(arr))
        target = A[-1]//3

        if not target % 1 == 0:
            return False
        
        i_set = set()
        first_i = None
        
        for i in range(N):
            if A[i] == target:
                i_set.add(i)
                if not first_i is not None:
                    first_i = i
                
        if first_i is not None:
            for i in range(first_i, N-1):
                for idx in i_set:
                    if i > idx and A[i] - A[idx] == target:
                        return True
                
        return False