class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        C = permutations([x for x in str(N)])
        for can in C:
            if can[0] != '0':
                x = ''.join(can)
                if math.log2(int(x)) % 1 == 0:
                    print(x)
                    return True
                
        return False