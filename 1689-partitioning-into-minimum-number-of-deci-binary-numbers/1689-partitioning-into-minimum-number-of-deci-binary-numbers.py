class Solution:
    def minPartitions(self, n: str) -> int:
        tmp = [int(x) for x in n]
        return max(tmp)
        #return max([int(x) for x in in n])