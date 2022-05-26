class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [int(x, 2) for x in bank]
        N = len(bank)
        cnt = 0
        ans = 0
        for x in bank:
            bc = x.bit_count()
            ans += cnt * bc
            if bc > 0:
                cnt = bc
        return ans