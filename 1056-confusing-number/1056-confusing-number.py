class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        good = '23457'
        for x in good:
            if x in n:
                return False
        ogn = n
        n = [x for x in n][::-1]
        
        for i in range(len(n)):
            if n[i] == '6':
                n[i] = '9'
            elif n[i] == '9':
                n[i] = '6'
        
        n = ''.join(n)
        #print(n)
        
        return ogn != n
                
        