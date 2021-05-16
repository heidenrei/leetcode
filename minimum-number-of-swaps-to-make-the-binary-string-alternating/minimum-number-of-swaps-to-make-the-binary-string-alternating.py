class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        ones1 = [i for i, _ in enumerate(s) if s[i] == '1']
        zeros1 = [i for i, _ in enumerate(s) if s[i] == '0']
        
        ones2 = ones1.copy()
        zeros2 = zeros1.copy()
        
        ones1 = [i for i in ones1 if not i & 1]
        zeros1 = [i for i in zeros1 if i & 1]
        
        ones2 = [i for i in ones2 if i & 1]
        zeros2 = [i for i in zeros2 if not i & 1]
        
        if len(ones1) == len(zeros1) and len(ones2) == len(zeros2):
            return min(len(ones1), len(ones2))
        
        if len(ones1) == len(zeros1):
            return len(ones1)
        
        if len(ones2) == len(zeros2):
            return len(ones2)
        
        return -1