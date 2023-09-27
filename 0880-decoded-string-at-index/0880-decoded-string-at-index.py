class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        curTapeLen = 0
        for c in S:
            o = ord(c) - 48
            if 0 <= o <= 9:
                newTapeLen = curTapeLen * o
                if K <= newTapeLen:
                    K %= curTapeLen
                    if K == 0:
                        K = curTapeLen
                    return self.decodeAtIndex(S, K)
                curTapeLen = newTapeLen
            else:
                curTapeLen += 1
                if curTapeLen == K:
                    return c