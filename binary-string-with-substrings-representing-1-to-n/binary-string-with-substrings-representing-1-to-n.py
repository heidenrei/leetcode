class Solution:
    def queryString(self, s: str, n: int) -> bool:
        num_bits = math.ceil(math.log(10**9, 2))
        N = len(s)
        nums = set()
        
        for i in range(1, num_bits+1):
            for j in range(N-i+1):
                nums.add(int(s[j:j+i], 2))
                print(s[j:j+i])
        for x in range(1, n+1):
            if x not in nums:
                return False
            
        return True